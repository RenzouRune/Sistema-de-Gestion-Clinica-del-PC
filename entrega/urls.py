from django.urls import path
from .views import reporte, verificar_entregas, comprobante

urlpatterns = [
    # Aquí puedes agregar tus rutas específicas de la app
    path('reporte/', reporte, name='reporte'),
    path('verificar/', verificar_entregas, name='verificar_entregas'),
    path('comprobante/', comprobante, name='comprobante'),
]
