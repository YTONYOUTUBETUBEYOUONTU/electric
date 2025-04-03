from rest_framework import serializers as Serializer
from .models import Cotizacion, CotizacionMaterial, CotizacionManoObra, Proyecto, Trabajo, Tarea

class CotizacionSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Cotizacion
        fields = '__all__'

class CotizacionMaterialSerializer(Serializer.ModelSerializer):
    class Meta:
        model = CotizacionMaterial
        fields = '__all__'

class CotizacionManoObraSerializer(Serializer.ModelSerializer):
    class Meta:
        model = CotizacionManoObra
        fields = '__all__'

class TrabajoSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Trabajo
        fields = '__all__'

class TareaSerializer(Serializer.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class ProyectoSerializer(Serializer.ModelSerializer):
    cotizacion_materiales = CotizacionMaterialSerializer(many=True, read_only=True)
    cotizacion_mano_obra = CotizacionManoObraSerializer(many=True, read_only=True)
    trabajos = TrabajoSerializer(many=True, read_only=True)
    Cotizaciones = CotizacionSerializer(many=True, read_only=True)
    tareas = TareaSerializer(many=True, read_only=True)
    
    class Meta:
        model = Proyecto
        fields = '__all__'
