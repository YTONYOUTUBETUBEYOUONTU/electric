from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.BooleanField(default=False)
    creado_en = models.DateTimeField()
    modificado_en = models.DateTimeField(auto_now=True)

class Cotizacion(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='cotizaciones', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    estado = models.BooleanField(default=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

class CotizacionMaterial(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, related_name='materiales', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

class CotizacionManoObra(models.Model):
    cotizacion = models.ForeignKey(Cotizacion, related_name='mano_obra', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=150)
    horas = models.IntegerField()
    precio_hora = models.DecimalField(max_digits=10, decimal_places=2)
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)



        
