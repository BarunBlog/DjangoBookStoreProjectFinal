import string
import random
import time
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import Permission
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from sslcommerz_python.payment import SSLCSession
from decimal import Decimal

from .models import Orders

# Create your views here.

def unique_transaction_id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class OrdersPageView(TemplateView):
    template_name = 'orders/purchase.html'

@login_required
def paymentRequest(request):
    #print(request.user.email)
            
    mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=settings.STORE_ID, sslc_store_pass=settings.STORE_PASSWORD)

    url_status = request.build_absolute_uri(reverse("payment_complete"))

    mypayment.set_urls(success_url=url_status, fail_url=url_status, cancel_url=url_status, ipn_url=url_status)
    
    mypayment.set_product_integration(total_amount=Decimal('39.00'), currency='BDT', product_category='e-books', product_name='book', num_of_item=100, shipping_method='NO', product_profile='None')

    mypayment.set_customer_info(name=f"{request.user}", email=f"{request.user.email}", address1='None', city='None', postcode='None', country='None', phone='None')

    mypayment.set_additional_values(value_a=f"{request.user}")
    response_data = mypayment.init_payment()

    return redirect(response_data['GatewayPageURL'])

@csrf_exempt
def paymentComplete(request):
    if request.method == 'POST':
        payment_data = request.POST
        status = payment_data['status']

        if status == 'VALID':
            Orders.objects.create(
                name = payment_data['value_a'],
                amount = payment_data['amount'],
                tran_id = payment_data['tran_id'],
                val_id = payment_data['val_id'],
                card_type = payment_data['card_type'],
                store_amount = payment_data['store_amount'],
                card_no = payment_data['card_no'],
                bank_tran_id = payment_data['bank_tran_id'],
                status = payment_data['status'],
                tran_date = payment_data['tran_date'],
                currency = payment_data['currency'],
                card_issuer = payment_data['card_issuer'],
                card_brand = payment_data['card_brand'],
                card_issuer_country = payment_data['card_issuer_country'],
                card_issuer_country_code = payment_data['card_issuer_country_code'],
                verify_sign = payment_data['verify_sign'],
                risk_level = payment_data['risk_level'],
                risk_title = payment_data['risk_title'],
            )
            
            return redirect(reverse("get_permission"))

        elif status == 'FAILED':
            return redirect(reverse("payment_failed"))
    
        elif status == 'CANCELLED':
            return redirect(reverse("orders"))


def paymentFailed(request):
    return render(request, 'orders/failed.html')


@login_required 
def getPermission(request):
    # Get the permission
    permission = Permission.objects.get(codename='special_status')

    # Get user
    u = request.user

    # Add to user's permission set
    u.user_permissions.add(permission)

    return render(request, 'orders/success.html')