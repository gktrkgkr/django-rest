from rest_framework import routers
from .views import vehicle_viewset

router = routers.DefaultRouter()
router.register('Vehicle', vehicle_viewset)