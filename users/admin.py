from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    auth_form = CustomUserCreationForm
    model = CustomUser
    form = CustomUserChangeForm
    list_display = ['is_staff', 'username', 'email', 'Nombre']

admin.site.register(CustomUser, CustomUserAdmin)



