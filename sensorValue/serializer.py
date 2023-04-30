from rest_framework import serializers
from sensorValue.models import SensorValue


class SensorValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorValue
        fields = '__all__'
