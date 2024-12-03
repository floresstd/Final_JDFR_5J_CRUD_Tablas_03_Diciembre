from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=255)
    Descripcion = models.CharField(max_length=255)
    Precio = models.DecimalField(max_digits=7, decimal_places=2)
    Stock = models.IntegerField()
    

    def __str__(self):
        return self.Nombre