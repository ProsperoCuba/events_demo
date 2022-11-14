from rest_framework.routers import DefaultRouter

from .views import ReservationViewSet

router = DefaultRouter()

# Endpoints for the module Events
router.register("reservations", ReservationViewSet, basename="reservations")

urlpatterns = [] + router.urls
