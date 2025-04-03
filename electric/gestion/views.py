from rest_framework import viewsets
from .models import Proyecto, Cotizacion, CotizacionMaterial, CotizacionManoObra, Trabajo, Tarea
from .serializers import ProyectoSerializer, TareaSerializer, CotizacionSerializer, CotizacionMaterialSerializer, CotizacionManoObraSerializer, TrabajoSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer
    
class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class CotizacionViewSet(viewsets.ModelViewSet):
    queryset = Cotizacion.objects.all()
    serializer_class = CotizacionSerializer

class CotizacionMaterialViewSet(viewsets.ModelViewSet):
    queryset = CotizacionMaterial.objects.all()
    serializer_class = CotizacionMaterialSerializer

class CotizacionManoDeObraViewSet(viewsets.ModelViewSet):
    queryset = CotizacionManoObra.objects.all()
    serializer_class = CotizacionManoObraSerializer

class TrabajoViewSet(viewsets.ModelViewSet):
    queryset = Trabajo.objects.all()
    serializer_class = TrabajoSerializer
