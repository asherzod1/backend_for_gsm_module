from django.db import models

# Create your models here.


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    building = models.ForeignKey('building.Building', on_delete=models.CASCADE, related_name='sensor')

    def __str__(self):
        return self.name
