from django.db import models

class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    Id_cliente = models.IntegerField()
    Fecha = models.DateField(null=True, blank=True)
    Id_producto = models.IntegerField()
    Id_Categoria = models.IntegerField()
    Cantidad = models.IntegerField()
    Precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Nuevo campo para el precio

    def __str__(self):
        return f"Orden #{self.id_orden}"

    @property
    def Total(self):
        return self.Cantidad * self.Precio
