
from django.db import models

# Create your models here.
class Movimiento(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cod_tp_pago = models.IntegerField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)

    def __str__(self):
        fila = "Descripcion: " + self.descripcion + "- Cantidad:" + str(self.cantidad) + "- Tipo " + str(self.cod_tp_pago)
        return fila
    
class Cierre_Diario(models.Model):
    id = models.AutoField(primary_key=True)
    Ing_efectivo = models.BigIntegerField(null=True, blank=True)
    Ing_POS = models.BigIntegerField(null=True, blank=True)
    Ing_transferencia = models.BigIntegerField(null=True, blank=True)
    Ing_abono = models.BigIntegerField(null=True, blank=True)
    fecha_cierre = models.DateField(null=True, blank=True)
    Ing_fondo = models.BigIntegerField(null=True, blank=True)
    def __str__(self):
        fila = "Fecha: " + self.fecha + "- Efectivo:" + str(self.Ing_efectivo) + "- POS " + str(self.Ing_POS)+ "- Trans. " + str(self.Ing_transferencia) + "- Abono " + str(self.Ing_transferencia)
        return fila

