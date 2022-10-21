from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm): #Campos a crear de usuario
    class Meta(UserCreationForm.Meta): #Meta = interno
        model = CustomUser #Determinar modelo
        fields = UserCreationForm.Meta.fields + ('Nombre','email', 'Tipo') #Usar campos predefinidos y agregar mas campos (nombre)
        #Modificar modelo primero en models.py


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields 