from django.db import models
from django.contrib.auth.models import User
from tkinter import CASCADE
##from django.contrib.auth.models import AbstractUser

class Tarea(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion= models.TextField(blank=True)
    fecha_creado=models.DateTimeField(auto_now_add=True)
    fecha_completados=models.DateTimeField(null=True)
    importante=models.BooleanField(default=False)
    usuarios= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo +'-by'+ self.User.username
# Create your models here.
