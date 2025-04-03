from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProyectoViewSet, TareaViewSet, CotizacionViewSet, CotizacionMaterialViewSet, CotizacionManoDeObraViewSet, TrabajoViewSet

router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)
router.register(r'Tarea', TareaViewSet)
router.register(r'cotizaciones', CotizacionViewSet)
router.register(r'cotizacion-materiales', CotizacionMaterialViewSet)
router.register(r'cotizacion-mano-obra', CotizacionManoDeObraViewSet)
router.register(r'trabajos', TrabajoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
