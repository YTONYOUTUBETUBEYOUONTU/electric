from django.contrib import admin
from .models import Proyecto, Cotizacion, CotizacionMaterial, CotizacionManoObra, Trabajo, Tarea

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Cotizacion)
admin.site.register(CotizacionMaterial)
admin.site.register(CotizacionManoObra)
admin.site.register(Trabajo)
admin.site.register(Tarea)


