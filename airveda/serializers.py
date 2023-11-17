from rest_framework import serializers
from .models import Device, TemperatureReading, HumidityReading

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['uid', 'name']

class TemperatureReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureReading
        fields = ['device', 'value', 'timestamp']

class HumidityReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumidityReading
        fields = ['device', 'value', 'timestamp']  # Ensure that 'value' is correct
