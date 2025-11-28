from django.urls import path
from . import views

urlpatterns = [
    path('recepcion/', views.recepcion_view, name='recepcion'),
    path('listado/', views.listado_equipos, name='listado_equipos'),
    path('detalle/<str:nombre>/', views.detalle_equipo, name='detalle_equipo'),
    path('editar_equipo/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('delete_equipo/<int:id>/', views.delete_equipo, name='delete_equipo'),
]
