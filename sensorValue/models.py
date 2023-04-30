from django.db import models

# Create your models here.


class SensorValue(models.Model):
    sensor = models.ForeignKey('sensor.Sensor', on_delete=models.CASCADE, related_name='values')
    description = models.TextField(null=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()
    temperature = models.FloatField()
    time = models.DateTimeField()

    def __str__(self):
        return str(self.time)

