from django.db import models

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True) 
    Nombre = models.CharField(max_length=200)
    Telefono = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    Direccion = models.TextField()
    

    def __str__(self):
        return self.Nombre