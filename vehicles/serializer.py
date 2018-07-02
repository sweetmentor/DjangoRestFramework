from rest_framework import serializers
from .models import Vehicle

class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="vehicle-detail")

    class Meta:
        model = Vehicle
        fields = ('url', 'id', 'registration',
                  'make', 'model', 'year')