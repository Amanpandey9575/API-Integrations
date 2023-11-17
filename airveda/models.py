from django.db import models

class Device(models.Model):
    uid = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)

class TemperatureReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class HumidityReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    value = models.FloatField()  
    timestamp = models.DateTimeField(auto_now_add=True)

