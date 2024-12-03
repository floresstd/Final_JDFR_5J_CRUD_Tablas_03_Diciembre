from django.db import models

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    Fecha_nacimiento = models.DateField(null=True, blank=True)
    Fecha_contratacion = models.DateField(null=True, blank=True)
    Puesto = models.CharField(max_length=50)
    

    def __str__(self):
        return self.Nombre