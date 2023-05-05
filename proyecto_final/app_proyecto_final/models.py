from django.db import models

from django.contrib.auth.models import User

#Limita la cantidad de digitos
from django.core.validators import MaxValueValidator, MinValueValidator

# ACÁ SE CREAN LAS TABLAS PARA LA DB SQLITE

# Create your models here.
class Sala(models.Model):
    nivel = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nivel} - {self.nombre}"   

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField(validators=[MaxValueValidator(99999999), MinValueValidator(10000000)])

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"  

class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.IntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"  

    
class Avatar(models.Model):

    imagen = models.ImageField(upload_to = "Avatars")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='proyecto_final_Avatars')


    