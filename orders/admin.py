from django.contrib import admin
#from django.db.models import Q
from django.utils.http import urlencode
from django.utils.html import format_html
from django.urls import reverse
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter

from .models import Order


# Django Admin Customization
admin.site.site_header = 'BookStore Admin Panel'
admin.site.site_title = 'Welcome to BookStore'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'tran_date', 'card_issuer_link', 'amount')
    list_filter = (
        ('tran_date', DateRangeFilter),
        ('card_brand', DropdownFilter),
        ('card_issuer', DropdownFilter)
    )
    search_fields = ("name", "card_type", "card_issuer")
    date_hierarchy = 'tran_date'

    def card_issuer_link(self, obj):
        url = (
            reverse("admin:orders_order_changelist")
            + "?"
            + urlencode({"q": f"{obj.card_issuer}"})
        )
        return format_html('<a href="{}">{}</a>', url, obj.card_issuer)
    
    card_issuer_link.short_description = "card issuer"

    '''def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct =  super().get_search_results(request, queryset, search_term)

        queryset |= self.model.objects.filter(
            Q(name__icontains=search_term) | 
            Q(card_issuer__icontains=search_term) |
            Q(card_type__icontains=search_term)
        )
        return queryset, use_distinct'''

admin.site.register(Order, OrderAdmin)
