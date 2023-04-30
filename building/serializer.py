from rest_framework import serializers
from building.models import Building


class BuildingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Building
        fields = '__all__'
