from rest_framework import serializers, viewsets

from ..models import Device, Address


# Serializers define the API representation.
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'name', 'email']


class DeviceSerializer(serializers.ModelSerializer):
    subscribers = AddressSerializer(many=True)

    class Meta:
        model = Device
        fields = ['id', 'name', 'subscribers']


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

