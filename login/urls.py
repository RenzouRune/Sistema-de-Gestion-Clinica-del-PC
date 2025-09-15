from django.urls import path
import login.views

urlpatterns = [
    # Aquí puedes agregar tus rutas específicas de la app
    path('logout/', login.views.logout_view, name='logout'),
]