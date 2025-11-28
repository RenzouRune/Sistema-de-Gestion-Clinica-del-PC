from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Asignacion, Diagnostico
from recepcion.models import Equipo

def asignar(request):
    if not request.session.get('autenticado'):
        return redirect('/')
    mensaje = ''
    estudiantes = Estudiante.objects.all()
    equipos_disponibles = Equipo.objects.filter(asignacion__isnull=True)

    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        equipo_id = request.POST.get('equipo')
        if estudiante_id and equipo_id:
            estudiante = Estudiante.objects.get(id=estudiante_id)
            equipo = Equipo.objects.get(id=equipo_id)
            if Asignacion.objects.filter(equipo=equipo).exists():
                mensaje = 'El equipo ya está asignado a otro estudiante.'
            else:
                Asignacion.objects.create(estudiante=estudiante, equipo=equipo)
                mensaje = 'Asignación realizada con éxito.'
        else:
            mensaje = 'Por favor, seleccione estudiante y equipo.'

    asignaciones = Asignacion.objects.all()
    return render(request, 'diagnostico/asignar.html', {
        'estudiantes': estudiantes,
        'equipos': equipos_disponibles,
        'asignaciones': asignaciones,
        'mensaje': mensaje,
    })

def evaluar(request):
    if not request.session.get('autenticado'):
        return redirect('/')
    mensaje = ''
    if request.method == 'POST':
        diagnostico = request.POST.get('diagnostico')
        solucion = request.POST.get('solucion')
        asignacion_id = request.POST.get('asignacion')
        if diagnostico and solucion and asignacion_id:
            asignacion = Asignacion.objects.get(id=asignacion_id)
            if Diagnostico.objects.filter(asignacion=asignacion).exists():
                mensaje = 'Este equipo ya tiene un diagnóstico.'
            else:
                Diagnostico.objects.create(asignacion=asignacion, diagnostico=diagnostico, solucion=solucion)
                mensaje = 'Diagnóstico y solución registrados con éxito.'
        else:
            mensaje = 'Por favor, complete todos los campos y seleccione una asignación.'
    asignaciones = Asignacion.objects.all()
    return render(request, 'diagnostico/evaluar.html', {'mensaje': mensaje, 'asignaciones': asignaciones})

def lista_diagnosticos(request):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    evaluaciones = Diagnostico.objects.all()
    return render(request, 'diagnostico/lista_de_diagnosticos.html', {'diagnosticos': evaluaciones})

def crear_estudiante(request):
    if not request.session.get('autenticado'):
        return redirect('/')
    mensaje = ''
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            if Estudiante.objects.filter(nombre=nombre).exists():
                mensaje = 'El estudiante ya existe.'
            else:
                Estudiante.objects.create(nombre=nombre)
                mensaje = 'Estudiante creado exitosamente.'
        else:
            mensaje = 'Por favor, ingrese un nombre.'
    return render(request, 'diagnostico/crear_estudiante.html', {'mensaje': mensaje})

def listar_estudiantes(request):
    if not request.session.get('autenticado'):
        return redirect('/')
    estudiantes = Estudiante.objects.all()
    return render(request, 'diagnostico/listar_estudiantes.html', {'estudiantes': estudiantes})

def editar_estudiante(request, id):
    if not request.session.get('autenticado'):
        return redirect('/')
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.nombre = request.POST.get('nombre')
        estudiante.save()
        return redirect('/diagnostico/diagnostico/listar_estudiantes/?mensaje=Estudiante actualizado exitosamente')
    return render(request, 'diagnostico/editar_estudiante.html', {'estudiante': estudiante})

def editar_asignacion(request, id):
    if not request.session.get('autenticado'):
        return redirect('/')
    asignacion = get_object_or_404(Asignacion, id=id)
    estudiantes = Estudiante.objects.all()
    equipos = Equipo.objects.all()
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        equipo_id = request.POST.get('equipo')
        if estudiante_id and equipo_id:
            asignacion.estudiante = Estudiante.objects.get(id=estudiante_id)
            asignacion.equipo = Equipo.objects.get(id=equipo_id)
            asignacion.save()
            return redirect('/diagnostico/diagnostico/asignar/?mensaje=Asignación actualizada exitosamente')
    return render(request, 'diagnostico/editar_asignacion.html', {'asignacion': asignacion, 'estudiantes': estudiantes, 'equipos': equipos})

def editar_diagnostico(request, id):
    if not request.session.get('autenticado'):
        return redirect('/')
    diagnostico = get_object_or_404(Diagnostico, id=id)
    if request.method == 'POST':
        diagnostico.diagnostico = request.POST.get('diagnostico')
        diagnostico.solucion = request.POST.get('solucion')
        diagnostico.save()
        return redirect('/diagnostico/diagnostico/lista/?mensaje=Diagnóstico actualizado exitosamente')
    return render(request, 'diagnostico/editar_diagnostico.html', {'diagnostico': diagnostico})

def delete_estudiante(request, id):
    if not request.session.get('autenticado'):
        return redirect('/')
    estudiante = get_object_or_404(Estudiante, id=id)
    estudiante.delete()
    return redirect('/diagnostico/diagnostico/listar_estudiantes/?mensaje=Estudiante eliminado exitosamente')

def delete_asignacion(request, id):
    if not request.session.get('autenticado'):
        return redirect('/')
    asignacion = get_object_or_404(Asignacion, id=id)
    asignacion.delete()
    return redirect('/diagnostico/diagnostico/asignar/?mensaje=Asignación eliminada exitosamente')

def delete_diagnostico(request, id):
    if not request.session.get('autenticado'):
        return redirect('/')
    diagnostico = get_object_or_404(Diagnostico, id=id)
    diagnostico.delete()
    return redirect('/diagnostico/diagnostico/lista/?mensaje=Diagnóstico eliminado exitosamente')
