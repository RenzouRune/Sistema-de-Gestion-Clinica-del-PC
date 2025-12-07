from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'recepcion/recepcion.html',{ "is_recepcion" :True })

def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('/')
    equipos = Equipo.objects.all()
    mensaje = request.GET.get('mensaje')
    return render(request, 'recepcion/listado.html', {'equipos': equipos, 'mensaje': mensaje, "is_recepcion" :True })

def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('/')
    equipo = Equipo.objects.filter(cliente=nombre).first()
    return render(request, 'recepcion/detalle.html', {'equipo': equipo, "is_recepcion" :True })

def editar_equipo(request, id):
    if not request.session.get('autenticado'):
        return redirect('/')
    equipo = get_object_or_404(Equipo, id=id)
    if request.method == 'POST':
        equipo.cliente = request.POST.get('cliente')
        equipo.tipo = request.POST.get('tipo')
        equipo.problema = request.POST.get('problema')
        equipo.save()
        return redirect('/recepcion/listado/?mensaje=Equipo actualizado exitosamente')
    return render(request, 'recepcion/editar_equipo.html', {'equipo': equipo, "is_recepcion" :True })

def delete_equipo(request, id):
    if not request.session.get('autenticado'):
        return redirect('/')
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    return redirect('/recepcion/listado/?mensaje=Equipo eliminado exitosamente')
