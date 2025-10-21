from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    id_marca = models.IntegerField()
    foto = models.ImageField(upload_to='productos/', null=True, blank=True)

    def __str__(self):
        return self.nombre
