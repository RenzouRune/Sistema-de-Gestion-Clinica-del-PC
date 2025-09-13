from django.shortcuts import render

asignaciones_globales = []

def asignar(request):
    mensaje = ''
    estudiantes = [
        {'nombre': 'matias'},
        {'nombre': 'cristal'},
        {'nombre': 'javier'},
        {'nombre': 'robin'},
        {'nombre': 'armando'},
    ]

    equipos = [
        {'nombre_equipo': 'equipo1'},
        {'nombre_equipo': 'equipo2'},
        {'nombre_equipo': 'equipo3'},
        {'nombre_equipo': 'equipo4'},
        {'nombre_equipo': 'equipo5'},
    ]

    asignaciones = []
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
