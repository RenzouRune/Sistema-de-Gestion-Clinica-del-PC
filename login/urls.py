from django.urls import path
import login.views

urlpatterns = [
    # Aquí puedes agregar tus rutas específicas de la app
    path('', login.views.login_view, name='login'),
    path('register/', login.views.register_view, name='register'),
    path('create_role/', login.views.create_role_view, name='create_role'),
    path('logout/', login.views.logout_view, name='logout'),
]
