from cv2 import VideoWriter_fourcc
from django import forms
from django.db import models

# Create your models here.
class Imagenes(models.Model):
    nombre = models.CharField(
        max_length=80,
        null= False,
        blank= False,
        unique= True
    )
    descripcion = models.CharField(
        max_length=100,
        null= False,
        blank= False,
        unique= False
    )
    def __str__(self):
        return self.nombre
    def save(self, **kwargs):
            
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        
        super(Imagenes, self).save()
    class Meta:
        verbose_name_plural ="Carreras"      
        
class Videos(models.Model):
    nombre = models.CharField(
        max_length=100,
        null= False,
        blank= False,
        unique= True
    )
    descripcion = models.CharField(
        max_length=100,
        null= False,
        blank= False,
        unique= False
    )
    def __str__(self):
        return self.nombre
    def save(self, **kwargs):
            
        self.nombre = self.nombre.upper()
        self.descripcion = self.descripcion.upper()
        super(Videos, self).save()
        

class Invitado(models.Model):
    correo = models.CharField(
        max_length=80,
        null= False,
        blank= False,
        unique= False
    )
    genero = models.CharField(
        max_length=80,
        null= False,
        blank= False,
        unique= False
    )
    edad = models.IntegerField()
    salario  = models.CharField(
        max_length=80,
        null= False,
        blank= False,
        unique= False
    )
    mac  = models.CharField(
        max_length=80,
        null= False,
        blank= False,
        unique= False
    )
    def __str__(self):
        return self.correo + " "+ self.genero + " " + self.edad + " " + self.salario + " " + self.mac
    def save(self, **kwargs):
            
        self.correo = self.correo.upper()
        self.genero = self.genero.upper()
        self.salario = self.salario.upper()
        self.mac = self.mac.upper()
        super(Invitado, self).save()
    class Meta:
        unique_together = ('correo','mac')
    
