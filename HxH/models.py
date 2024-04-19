from django.db import models

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    habilidades = models.ManyToManyField('Habilidad', related_name='personajes')

    def __str__(self):
        return self.nombre

class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="Sin descripcion disponible")
    categoria = models.ForeignKey('CategoriaHabilidad', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class CategoriaHabilidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
