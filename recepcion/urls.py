from django.urls import path
from . import views

urlpatterns = [
    path('recepcion/', views.recepcion_view, name='recepcion'),
]