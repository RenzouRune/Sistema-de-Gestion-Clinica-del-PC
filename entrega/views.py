from django.shortcuts import redirect, render
from .models import Reporte
from diagnostico.models import Asignacion, Diagnostico
from recepcion.models import Equipo

def reporte(request):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    mensaje = ''
    if request.method == 'POST':
        asignacion_id = request.POST.get('asignacion')
        estado = request.POST.get('estado')
        if asignacion_id and estado:
            asignacion = Asignacion.objects.get(id=asignacion_id)
            if not Diagnostico.objects.filter(asignacion=asignacion).exists():
                mensaje = 'La asignación seleccionada no tiene un diagnóstico realizado.'
            elif Reporte.objects.filter(asignacion=asignacion).exists():
                mensaje = 'Ya existe un reporte para esta asignación.'
            else:
                Reporte.objects.create(asignacion=asignacion, estado=estado)
                mensaje = 'Reporte registrado con éxito.'
        else:
            mensaje = 'Por favor, seleccione una asignación y un estado.'
    asignaciones = Asignacion.objects.all()
    diagnosticos = Diagnostico.objects.all()
    reportes = Reporte.objects.all()
    return render(request, 'entrega/reporte.html', {
        'asignaciones': asignaciones,
        'diagnosticos': diagnosticos,
        'reportes': reportes,
        'mensaje': mensaje
    })

def verificar_entregas(request):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    clientes = Equipo.objects.values_list('cliente', flat=True).distinct()
    mensaje = ''
    reportes_cliente = []
    if request.method == 'GET' and 'cliente' in request.GET:
        cliente = request.GET.get('cliente')
        reportes_cliente = Reporte.objects.filter(asignacion__equipo__cliente=cliente)
        if not reportes_cliente:
            mensaje = 'Los equipos de este cliente no han sido reportados aún.'
    return render(request, 'entrega/verificar.html', {
        'clientes': clientes,
        'reportes_cliente': reportes_cliente,
        'mensaje': mensaje
    })

def comprobante(request):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    cliente = request.GET.get('cliente')
    equipo_id = request.GET.get('equipo')
    context = {}
    if cliente and equipo_id:
        try:
            equipo = Equipo.objects.get(id=equipo_id, cliente=cliente)
            reporte = Reporte.objects.filter(asignacion__equipo=equipo).first()
            diagnostico = Diagnostico.objects.filter(asignacion__equipo=equipo).first()
            if reporte and diagnostico:
                context = {
                    'cliente': cliente,
                    'equipo': equipo.tipo,
                    'diagnostico': diagnostico.diagnostico,
                    'solucion': diagnostico.solucion,
                    'estado': reporte.estado
                }
            else:
                context = {'error': 'No se encontró la información'}
        except Equipo.DoesNotExist:
            context = {'error': 'Equipo no encontrado'}
    else:
        context = {'error': 'Parámetros inválidos'}
    return render(request, 'entrega/comprobante.html', context)
