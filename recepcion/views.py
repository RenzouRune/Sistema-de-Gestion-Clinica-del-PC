from django.shortcuts import render, redirect
from .data_store import equipos


def recepcion_view(request):
    if not request.session.get('autenticado'):
        return redirect('')
    mensaje = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        tipo = request.POST.get('tipo')
        problema = request.POST.get('problema')
        equipos.append({'nombre': nombre, 'tipo': tipo, 'problema': problema})
        mensaje = 'Equipo registrado exitosamente'
    return render(request, 'recepcion/recepcion.html', {'mensaje': mensaje})

def listado_equipos(request):
    if not request.session.get('autenticado'):
        return redirect('/login/')
    return render(request, 'recepcion/listado.html', {'equipos': equipos})

def detalle_equipo(request, nombre):
    if not request.session.get('autenticado'):
        return redirect('/login/')
    equipo = next((e for e in equipos if e['nombre'] == nombre), None)
    return render(request, 'recepcion/detalle.html', {'equipo': equipo})