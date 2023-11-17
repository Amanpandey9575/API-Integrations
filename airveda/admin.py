from django.contrib import admin
from .models import Device, TemperatureReading, HumidityReading

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name')
    search_fields = ('uid', 'name')

class TemperatureReadingAdmin(admin.ModelAdmin):
    list_display = ['device', 'value', 'timestamp'] 

admin.site.register(TemperatureReading, TemperatureReadingAdmin)

class HumidityReadingAdmin(admin.ModelAdmin):
    list_display = ['device', 'value', 'timestamp']
    search_fields = ['device__name']

admin.site.register(HumidityReading, HumidityReadingAdmin)

