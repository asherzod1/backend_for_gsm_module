from django.db import models

# Create your models here.


class Building(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    longitude = models.FloatField()
    latitude = models.FloatField()


    def __str__(self):
        return self.name
