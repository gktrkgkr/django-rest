from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import vehicle_serializer, vehicle_create_serializer
from .models import Vehicle
from django.core.cache import cache

class vehicle_viewset(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = vehicle_serializer

@api_view(['GET'])
def get_vehicle(request, pk):
    pk_str = str(pk)
    cacheF = cache.get('vehicle_id_'+ pk_str)
    if( cacheF == None):
        vehicle = Vehicle.objects.get(id=pk)
        serializer = vehicle_serializer(vehicle)
        cache.set('vehicle_id_'+ pk_str, serializer.data, 6000)
        data = serializer.data
    else:
        data = cache.get('vehicle_id_'+ pk_str)
    return Response(data)

@api_view(['POST'])
def create_vehicle(request):
    serializer = vehicle_create_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    data = serializer.data
    return Response(data)

@api_view(['POST'])
def update_vehicle(request, pk):
    pk_str = str(pk)
    vehicle = Vehicle.objects.get(id=pk)
    serializer = vehicle_create_serializer(instance=vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save()
        cache.set('vehicle_id_'+ pk_str, serializer.data, 6000)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_vehicle(request, pk):
    pk_str = str(pk)
    vehicle = Vehicle.objects.get(id=pk)
    cache.delete('vehicle_id_'+ pk_str)
    vehicle.delete()
    
    return Response("Item deleted!")

