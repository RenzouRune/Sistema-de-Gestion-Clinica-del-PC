from django.urls import path
from . import views

urlpatterns = [
    path('diagnostico/asignar/', views.asignar, name='asignar_estudiante'),
    path('diagnostico/evaluar/', views.evaluar, name='evaluar'),
    path('diagnostico/lista/', views.lista_diagnosticos, name='lista_diagnosticos'),
    path('diagnostico/crear_estudiante/', views.crear_estudiante, name='crear_estudiante'),
    path('diagnostico/listar_estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('diagnostico/editar_estudiante/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('diagnostico/editar_asignacion/<int:id>/', views.editar_asignacion, name='editar_asignacion'),
    path('diagnostico/editar_diagnostico/<int:id>/', views.editar_diagnostico, name='editar_diagnostico'),
]
