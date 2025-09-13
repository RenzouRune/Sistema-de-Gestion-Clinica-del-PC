from django.urls import path
from . import views

urlpatterns = [
    path('diagnostico/asignar/', views.asignar, name='asignar_estudiante'),
]