from django.contrib import admin
from django.urls import path, include
from login.views import *
from recepcion.views import *
from entrega.views import *
from diagnostico.views import *

urlpatterns = [
    path('', login_view, name='inicio'), 
    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    path('recepcion/', include('recepcion.urls')),
    path('entrega/', include('entrega.urls')),
    path('diagnostico/', include('diagnostico.urls')),
]
