from django.urls import path
from . import views

urlpatterns = [
    path('diagnostico/asignar/', views.asignar, name='asignar_estudiante'),
    path('diagnostico/evaluar/', views.evaluar, name='evaluar'),
    path('diagnostico/lista/', views.lista_diagnosticos, name='lista_diagnosticos'),
]
