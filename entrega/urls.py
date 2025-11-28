from django.urls import path
from .views import reporte, verificar_entregas, comprobante, editar_reporte, delete_reporte

urlpatterns = [
    # Aquí puedes agregar tus rutas específicas de la app
    path('reporte/', reporte, name='reporte'),
    path('verificar/', verificar_entregas, name='verificar_entregas'),
    path('comprobante/', comprobante, name='comprobante'),
    path('editar_reporte/<int:id>/', editar_reporte, name='editar_reporte'),
    path('delete_reporte/<int:id>/', delete_reporte, name='delete_reporte'),
]
