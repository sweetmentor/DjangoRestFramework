from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from.serializers import VehicleSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'vehicles': reverse('vehicle-list', request=request, format=format)
    })

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer