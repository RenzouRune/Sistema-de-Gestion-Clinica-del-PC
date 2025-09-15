from django.shortcuts import redirect, render
from diagnostico.views import asignaciones_globales, evaluaciones_globales
from recepcion.data_store import equipos

entregas_globales = [
    {'estudiante': 'matias', 'equipo': 'Desktop', 'cliente': 'Juan Vargas', 'estado': 'Entregado'},
    {'estudiante': 'cristal', 'equipo': 'Laptop', 'cliente': 'Maria Sanchez', 'estado': 'Pendiente'},
    {'estudiante': 'javier', 'equipo': 'Tablet', 'cliente': 'Pedro Alvarado', 'estado': 'Entregado'},
    {'estudiante': 'robin', 'equipo': 'All-in-One', 'cliente': 'Ana Torres', 'estado': 'Entregado'},
    {'estudiante': 'armando', 'equipo': 'Notebook', 'cliente': 'Luis Fuentes', 'estado': 'Pendiente'},
]

def reporte(request):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    mensaje = ''
    if request.method == 'POST':
        asignacion_index = request.POST.get('asignacion')
        estado = request.POST.get('estado')
        if asignacion_index and estado and asignacion_index.isdigit():
            index = int(asignacion_index)
            if 0 <= index < len(asignaciones_globales):
                asignacion = asignaciones_globales[index]
                # Verificar si tiene diagnóstico
                tiene_diagnostico = any(
                    e['estudiante'] == asignacion['estudiante']['nombre'] and
                    e['equipo'] == asignacion['equipo']['nombre_equipo']
                    for e in evaluaciones_globales
                )
                if not tiene_diagnostico:
                    mensaje = 'La asignación seleccionada no tiene un diagnóstico realizado.'
                else:
                    equipo_obj = next((e for e in equipos if e['tipo'] == asignacion['equipo']['nombre_equipo']), None)
                    if equipo_obj:
                        cliente = equipo_obj['nombre']
                    else:
                        cliente = 'Cliente no encontrado'
                    entrega_dict = {
                        'estudiante': asignacion['estudiante']['nombre'],
                        'equipo': asignacion['equipo']['nombre_equipo'],
                        'cliente': cliente,
                        'estado': estado
                    }
                    entregas_globales.append(entrega_dict)
                    mensaje = 'Reporte registrado con éxito.'
            else:
                mensaje = 'Asignación inválida.'
        else:
            mensaje = 'Por favor, seleccione una asignación y un estado.'
    return render(request, 'entrega/reporte.html', {
        'asignaciones': asignaciones_globales,
        'evaluaciones': evaluaciones_globales,
        'entregas': entregas_globales,
        'mensaje': mensaje
    })


def verificar_entregas(request):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    clientes = list(set(e['nombre'] for e in equipos))
    mensaje = ''
    entregas_cliente = []
    if request.method == 'GET' and 'cliente' in request.GET:
        cliente = request.GET.get('cliente')
        entregas_cliente = [e for e in entregas_globales if e['cliente'] == cliente]
        if not entregas_cliente:
            mensaje = 'los equipos de este cliente no han sido reportados aun'
    return render(request, 'entrega/verificar.html', {
        'clientes': clientes,
        'entregas_cliente': entregas_cliente,
        'mensaje': mensaje
    })

def comprobante(request):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    cliente = request.GET.get('cliente')
    equipo = request.GET.get('equipo')
    context = {}
    if cliente and equipo:
        entrega = next((e for e in entregas_globales if e['cliente'] == cliente and e['equipo'] == equipo), None)
        evaluacion = next((ev for ev in evaluaciones_globales if ev['equipo'] == equipo), None)
        if entrega and evaluacion:
            context = {
                'cliente': cliente,
                'equipo': equipo,
                'diagnostico': evaluacion['diagnostico'],
                'solucion': evaluacion['solucion'],
                'estado': entrega['estado']
            }
        else:
            context = {'error': 'No se encontró la información'}
    else:
        context = {'error': 'Parámetros inválidos'}
    return render(request, 'entrega/comprobante.html', context)
