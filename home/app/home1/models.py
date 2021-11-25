from django.db import models

# Create your models here.
class prueba(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=255)
    edad = models.CharField(max_length=20)
    sexo = models.CharField(max_length=20)

    def str(self):
        return "{0}".format(self.nombre)