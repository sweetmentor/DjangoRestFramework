from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .serializers import VehicleSerializer
from .models import Vehicle

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'vehicles': reverse('vehicle-list', request=request, format=format)
    })

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    
    def get_object(self):
        obj = get_object_or_404(Vehicle.objects.all(), pk=self.kwargs['pk'])
        return obj