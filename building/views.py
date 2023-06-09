from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from building.models import Building
from building.serializer import BuildingSerializer
from sensor.serializer import SensorSerializer


class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        res = serializer.data
        res["sensors"] = SensorSerializer(instance.sensor.all(), many=True).data
        return Response(res)
