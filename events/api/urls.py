from rest_framework.routers import DefaultRouter

from .views import EventViewSet

router = DefaultRouter()

# Endpoints for the module Events
router.register("events", EventViewSet, basename="events")

urlpatterns = [] + router.urls
