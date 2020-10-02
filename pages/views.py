from django.shortcuts import render
from django.views.generic import TemplateView
from allauth.account.views import PasswordChangeView
from django.urls import reverse

# Create your views here.
'''
We can leverage Django’s built-in TemplateView so
that the only tweak needed is to specify our desired template, home.html
'''
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CustomPasswordChangeView(PasswordChangeView):
    success_url = '/'