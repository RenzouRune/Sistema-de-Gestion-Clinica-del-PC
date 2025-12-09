from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Equipo
from .serializers import EquipoSerializer
from rest_framework import status


@api_view(['GET'])
def api_lista_equipos(request):
    equipos = Equipo.objects.all()
    serializer = EquipoSerializer(equipos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def api_registrar_equipo(request):
    serializer = EquipoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def api_modificar_equipo(request, pk):
    try:
        equipo = Equipo.objects.get(pk=pk)
    except Equipo.DoesNotExist:
        return Response({'error':'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = EquipoSerializer(equipo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def api_eliminar_equipo(request, pk):
    try:
        equipo = Equipo.objects.get(pk=pk)
    except Equipo.DoesNotExist:
        return Response({'error':'Equipo no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    equipo.delete()
    return Response({'message': 'Equipo eliminado correctamente'}, status=status.HTTP_200_OK)