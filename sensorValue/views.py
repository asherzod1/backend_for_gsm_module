from rest_framework.viewsets import ModelViewSet
from sensorValue.models import SensorValue
from sensorValue.serializer import SensorValueSerializer


class SensorValueViewSet(ModelViewSet):
    queryset = SensorValue.objects.all()
    serializer_class = SensorValueSerializer
