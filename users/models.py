from distutils.text_file import TextFile
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    Encargado = 'Encargado'
    Supervisor = 'Supervisor'
    Administrador = 'Administrador'
    Nombre = models.CharField(max_length = 15)
    TiposUsuario = [
        (Encargado, 'Encargado'),
        (Supervisor, 'Supervisor'),
        (Administrador, 'Administrador'),
    ]
    Tipo = models.CharField(
        max_length=13,
        choices=TiposUsuario,
        default=Encargado,
    )
   