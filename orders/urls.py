from django.urls import path

from .views import OrdersPageView, paymentRequest, paymentComplete, paymentFailed, getPermission

urlpatterns = [
    path('', OrdersPageView.as_view(), name='orders'),
    path('payment_request', paymentRequest, name='payment_request'),
    path('payment_complete', paymentComplete, name='payment_complete'),
    path('payment_failed', paymentFailed, name='payment_failed'),
    path('get_permission', getPermission, name='get_permission'),
]