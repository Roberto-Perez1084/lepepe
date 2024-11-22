from django.db import models

# Create your models here.

class Sucursal(models.Model):
    id_sucursal=models.models.CharField(primary_key=True, max_length=6)
    nombre_suc=models.CharField(max_length=20)
    direccion_suc=models.CharField(max_length=100)
    horario_suc=models.CharField(max_length=20)
    email_suc=models.CharField(max_length=50)
    tel_suc=models.CharField(max_length=14)
    gerente_suc=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_suc