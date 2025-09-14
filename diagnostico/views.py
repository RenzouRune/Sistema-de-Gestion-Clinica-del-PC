from django.shortcuts import render
from recepcion.data_store import equipos

asignaciones_globales = []

def asignar(request, equipos=equipos):
    mensaje = ''
    estudiantes = [
        {'nombre': 'matias'},
        {'nombre': 'cristal'},
        {'nombre': 'javier'},
        {'nombre': 'robin'},
        {'nombre': 'armando'},
    ]

    equipos = [{'nombre_equipo': e['tipo']} for e in equipos]

    
    estudiante_recibido = request.GET.get('estudiante')
    equipo_recibido = request.GET.get('equipo')
    if estudiante_recibido and equipo_recibido:            

        estudiante = next(e for e in estudiantes if e['nombre'] == estudiante_recibido)
        equipo = next(e for e in equipos if e['nombre_equipo'] == equipo_recibido)

        asignaciones_globales.append({'estudiante': estudiante, 'equipo': equipo})
        mensaje = 'Asignación realizada con éxito.'

    return render(request, 'diagnostico/asignar.html', {
        'estudiantes': estudiantes,
        'equipos': equipos,
        'asignaciones': asignaciones_globales,
        'mensaje': mensaje,
    })
