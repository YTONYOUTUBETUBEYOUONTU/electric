from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.BooleanField(default=False)
    creado_en = models.DateTimeField()
    modificado_en = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

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

class Trabajo(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='trabajos', on_delete=models.CASCADE)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    
class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='tareas', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    responsable = models.CharField(max_length=100, blank=True, null=True)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField(blank=True, null=True)
    completa = models.BooleanField(default=False)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre + ' ' + self.proyecto.nombre
