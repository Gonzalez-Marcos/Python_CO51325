from django.db import models

from django.contrib.auth.models import User

# ACÁ SE CREAN LAS TABLAS PARA LA DB SQLITE

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.comision}"   

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"  

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"  

class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} - {self.fecha_entrega}"  
    
class Avatar(models.Model):

    imagen = models.ImageField(upload_to = "Avatars")
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='proyecto_final_Avatars')


    