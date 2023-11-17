from rest_framework import viewsets
from .models import Device, TemperatureReading, HumidityReading
from .serializers import DeviceSerializer, TemperatureReadingSerializer, HumidityReadingSerializer
from django.shortcuts import render
from django.views import View
from .models import Device, TemperatureReading, HumidityReading
from django.http import HttpResponseNotFound

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class TemperatureReadingViewSet(viewsets.ModelViewSet):
    queryset = TemperatureReading.objects.all()
    serializer_class = TemperatureReadingSerializer

class HumidityReadingViewSet(viewsets.ModelViewSet):
    queryset = HumidityReading.objects.all()
    serializer_class = HumidityReadingSerializer


# class DeviceGraphView(View):
#     template_name = 'devices_graph.html'

#     def get(self, request,uid, *args, **kwargs):
#         try:
#             device = Device.objects.get(uid=uid)
#             print("device - ",device)
#             device_uid = device.uid
#             print(device_uid)

#             device_name = device.name

#             temperature_readings = TemperatureReading.objects.get(device=device)
#             temp_device = temperature_readings.value
#             temp_time = temperature_readings.timestamp

#             humidity_readings = HumidityReading.objects.get(device=device)
#             humidity = humidity_readings.value
#             humidity_time = humidity_readings.timestamp

#             if temperature_readings.count() > 1 or humidity_readings.count() > 1:

#                 return HttpResponseNotFound("Multiple readings found for the device.")

#             # Assuming there's only one reading for each type
#             temperature_reading = temperature_readings.first()
#             humidity_reading = humidity_readings.first()

#             return render(request, self.template_name, {
#                 'uid': uid,
#                 'device_name':device_name,
#                 'temperature_readings': temperature_readings,
#                 'humidity_readings': humidity_readings,
#                 'temp_device':temp_device,
#                 'humidity':humidity,
#                 'temp_time':temp_time,
#                 'humidity_time':humidity_time

#             })
#         except Device.DoesNotExist:
#             return HttpResponseNotFound("Device not found.")


from django.views import View
from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Device, TemperatureReading, HumidityReading

class DeviceGraphView(View):
    template_name = 'devices_graph.html'

    def get(self, request, uid, *args, **kwargs):
        try:
            device = Device.objects.get(uid=uid)
            device_name = device.name

            # Use filter() instead of get() for multiple objects
            temperature_readings = TemperatureReading.objects.filter(device=device)
            humidity_readings = HumidityReading.objects.filter(device=device)

            # Check if there are multiple objects returned
            if temperature_readings.count() > 1 or humidity_readings.count() > 1:
                return HttpResponseNotFound("Multiple readings found for the device.")

            # Assuming there's only one reading for each type
            temperature_reading = temperature_readings.first()
            humidity_reading = humidity_readings.first()

            if temperature_reading is None:
                return HttpResponseNotFound("Temperature reading not found for the device.")

            if humidity_reading is None:
                return HttpResponseNotFound("Humidity reading not found for the device.")

            temp_device = temperature_reading.value
            temp_time = temperature_reading.timestamp

            humidity = humidity_reading.value
            humidity_time = humidity_reading.timestamp

            return render(request, self.template_name, {
                'uid': uid,
                'device_name': device_name,
                'temperature_readings': temperature_readings,
                'humidity_readings': humidity_readings,
                'temp_device': temp_device,
                'humidity': humidity,
                'temp_time': temp_time,
                'humidity_time': humidity_time
            })

        except Device.DoesNotExist:
            return HttpResponseNotFound("Device not found.")
