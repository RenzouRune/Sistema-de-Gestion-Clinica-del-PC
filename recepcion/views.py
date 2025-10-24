from django.shortcuts import render, redirect
from .models import Equipo

def recepcion_view(request):
    if not request.session.get('autenticado'):
        return redirect('/')
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        tipo = request.POST.get('tipo')
        problema = request.POST.get('problema')
        Equipo.objects.create(cliente=cliente, tipo=tipo, problema=problema)
        return redirect('/recepcion/listado/?mensaje=Equipo registrado exitosamente')
    return render(request, 'recepcion/recepcion.html')

def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('/')
    equipos = Equipo.objects.all()
    mensaje = request.GET.get('mensaje')
    return render(request, 'recepcion/listado.html', {'equipos': equipos, 'mensaje': mensaje})

def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('/')
    equipo = Equipo.objects.filter(cliente=nombre).first()
    return render(request, 'recepcion/detalle.html', {'equipo': equipo})
