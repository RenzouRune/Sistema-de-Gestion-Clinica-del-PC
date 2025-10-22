from django.urls import path
from . import views

urlpatterns = [
    path('diagnostico/asignar/', views.asignar, name='asignar_estudiante'),
    path('diagnostico/evaluar/', views.evaluar, name='evaluar'),
    path('diagnostico/lista/', views.lista_diagnosticos, name='lista_diagnosticos'),
    path('diagnostico/crear_estudiante/', views.crear_estudiante, name='crear_estudiante'),
    path('diagnostico/listar_estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
]
