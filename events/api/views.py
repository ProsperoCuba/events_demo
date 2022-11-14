from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from core.enums import EventType
from events.api.serializers import EventSerializer, EventDetailsSerializer
from events.models import Event


# ViewSet for the model Event
class EventViewSet(ModelViewSet):
    """ViewSet to model Event"""
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = (DjangoModelPermissions, IsAuthenticated)

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return self.queryset.filter(type=EventType.public)

        return self.queryset

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EventDetailsSerializer

        return self.serializer_class
