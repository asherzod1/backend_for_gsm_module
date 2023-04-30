from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from sensor.models import Sensor
from sensor.serializer import SensorSerializer
from sensorValue.serializer import SensorValueSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        res = serializer.data
        res["values"] = SensorValueSerializer(instance.values.all(), many=True).data
        return Response(res)
