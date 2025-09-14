from django.shortcuts import render
from recepcion.data_store import equipos

asignaciones_globales = []
evaluaciones_globales = []

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

    assigned_equipos = {a['equipo']['nombre_equipo'] for a in asignaciones_globales}
    equipos_disponibles = [e for e in equipos if e['nombre_equipo'] not in assigned_equipos]

    estudiante_recibido = request.GET.get('estudiante')
    equipo_recibido = request.GET.get('equipo')
    
    if estudiante_recibido and equipo_recibido:
        if any(a['equipo']['nombre_equipo'] == equipo_recibido for a in asignaciones_globales):
            mensaje = 'El equipo ya está asignado a otro estudiante.'
        else:
            estudiante = next(e for e in estudiantes if e['nombre'] == estudiante_recibido)
            equipo = next(e for e in equipos if e['nombre_equipo'] == equipo_recibido)

            asignaciones_globales.append({'estudiante': estudiante, 'equipo': equipo})
            mensaje = 'Asignación realizada con éxito.'

    return render(request, 'diagnostico/asignar.html', {
        'estudiantes': estudiantes,
        'equipos': equipos_disponibles,
        'asignaciones': asignaciones_globales,
        'mensaje': mensaje,
    })

def evaluar(request):
    mensaje = ''
    if request.method == 'POST':
        diagnostico = request.POST.get('diagnostico')
        solucion = request.POST.get('solucion')
        asignacion_index = request.POST.get('asignacion')
        if diagnostico and solucion and asignacion_index and asignacion_index.isdigit():
            index = int(asignacion_index)
            if 0 <= index < len(asignaciones_globales):
                asignacion = asignaciones_globales[index]
                evaluacion = {
                    'estudiante': asignacion['estudiante']['nombre'],
                    'equipo': asignacion['equipo']['nombre_equipo'],
                    'diagnostico': diagnostico,
                    'solucion': solucion
                }
                evaluaciones_globales.append(evaluacion)
                mensaje = 'Diagnóstico y solución registrados con éxito.'
            else:
                mensaje = 'Asignación inválida.'
        else:
            mensaje = 'Por favor, complete todos los campos y seleccione una asignación.'
    return render(request, 'diagnostico/evaluar.html', {'mensaje': mensaje, 'asignaciones': asignaciones_globales})

def lista_diagnosticos(request):
    return render(request, 'diagnostico/lista_de_diagnosticos.html', {'evaluaciones': evaluaciones_globales})
