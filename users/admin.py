from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

'''
We’ll extend the existing UserAdmin into CustomUserAdmin and tell Django to use our
new forms, custom user model, and list only the email and username of a user. If we
wanted to we could add more of the existing User fields to list_display such as
is_staff.
'''

CustomUser = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm

    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)

