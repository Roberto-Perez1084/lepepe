from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto=models.CharField(primary_key=True, max_length=6)
    nom_producto=models.CharField(max_length=20)
    tipo_producto=models.CharField(max_length=10)
    cant_producto=models.CharField(max_length=5)
    metodo_pag=models.CharField(max_length=15)
    proveedor_prod=models.CharField(max_length=15)
    id_proveedor=models.CharField(max_length=15)

    def __str__(self):
        return self.nom_producto
