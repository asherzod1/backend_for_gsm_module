from rest_framework import routers
from building.views import BuildingViewSet
from sensor.views import SensorViewSet
from sensorValue.views import SensorValueViewSet

router:routers.DefaultRouter = routers.DefaultRouter()
# router.register('users',UserViewSet,basename='users')
router.register('building', BuildingViewSet, basename='building')
router.register('sensor', SensorViewSet, basename='sensor')
router.register('sensor-value', SensorValueViewSet, basename='sensorValue')
