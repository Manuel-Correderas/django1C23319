from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class Usuarios(models.Model):
    # Agrega campos adicionales aquí según tus necesidades
    # Por ejemplo:
    nombre_user=models.CharField(null=False,verbose_name='Nombre',max_length=50)
    Dni_Id_user= models.IntegerField(null=False)
    
    telefono_user = models.IntegerField(null=False)
    email_user = models.EmailField(null=False,max_length=50)
    def __str__(self):
        return self.nombre_user
    class Meta:
        db_table='usuarios'
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        ordering=['id']
from django.db import models

class Consulta(models.Model):
    TIPO_CONSULTA = (
        (1, 'Oferta del día'),
        (2, 'Comprar en cantidad'),
        (3, 'Oferta para compartir'),
    )

    nombre = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField(max_length=500)
    tipo_consulta = models.IntegerField(choices=TIPO_CONSULTA)
    suscripcion = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


