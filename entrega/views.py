from django.shortcuts import redirect, render, get_object_or_404
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
            diagnostico = Diagnostico.objects.filter(asignacion=asignacion).first()
            if not diagnostico:
                mensaje = 'La asignación seleccionada no tiene un diagnóstico realizado.'
            elif Reporte.objects.filter(diagnostico=diagnostico).exists():
                mensaje = 'Ya existe un reporte para esta asignación.'
            else:
                Reporte.objects.create(diagnostico=diagnostico, estado=estado)
                mensaje = 'Reporte registrado con éxito.'
        else:
            mensaje = 'Por favor, seleccione una asignación y un estado.'
    asignaciones = Asignacion.objects.all()
    evaluaciones = Diagnostico.objects.all()
    entregas = Reporte.objects.all()
    return render(request, 'entrega/reporte.html', {
        'asignaciones': asignaciones,
        'diagnosticos': evaluaciones,
        'reportes': entregas,
        'mensaje': mensaje,
        "is_entrega": True
    })

def verificar_entregas(request):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    clientes = Equipo.objects.values_list('cliente', flat=True).distinct()
    mensaje = ''
    reportes_cliente = []
    if request.method == 'GET' and 'cliente' in request.GET:
        cliente = request.GET.get('cliente')
        reportes_cliente = Reporte.objects.filter(diagnostico__asignacion__equipo__cliente=cliente)
        if not reportes_cliente:
            mensaje = 'Los equipos de este cliente no han sido reportados aún.'
    return render(request, 'entrega/verificar.html', {
        'clientes': clientes,
        'reportes_cliente': reportes_cliente,
        'mensaje': mensaje,
        "is_entrega": True
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
            entrega = Reporte.objects.filter(diagnostico__asignacion__equipo=equipo).first()
            evaluacion = Diagnostico.objects.filter(asignacion__equipo=equipo).first()
            if entrega and evaluacion:
                context = {
                    'cliente': cliente,
                    'equipo': equipo.tipo,
                    'diagnostico': evaluacion.diagnostico,
                    'solucion': evaluacion.solucion,
                    'estado': entrega.estado
                }
            else:
                context = {'error': 'No se encontró la información'}
        except Equipo.DoesNotExist:
            context = {'error': 'Equipo no encontrado'}
    else:
        context = {'error': 'Parámetros inválidos'}
    return render(request, 'entrega/comprobante.html', context={**context, "is_entrega": True})

def editar_reporte(request, id):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    reporte = get_object_or_404(Reporte, id=id)
    if request.method == 'POST':
        estado = request.POST.get('estado')
        if estado:
            reporte.estado = estado
            reporte.save()
            return redirect('/entrega/reporte/?mensaje=Reporte actualizado exitosamente')
    return render(request, 'entrega/editar_reporte.html', {'reporte': reporte, "is_entrega": True})

def delete_reporte(request, id):
    if not request.session.get('autenticado'):
        return redirect('inicio')
    reporte = get_object_or_404(Reporte, id=id)
    reporte.delete()
    return redirect('/entrega/reporte/?mensaje=Reporte eliminado exitosamente')
