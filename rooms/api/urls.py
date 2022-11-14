from rest_framework.routers import DefaultRouter

from .views import RoomViewSet

router = DefaultRouter()

# Endpoints for the module Rooms
router.register("rooms", RoomViewSet, basename="rooms")

urlpatterns = [] + router.urls
