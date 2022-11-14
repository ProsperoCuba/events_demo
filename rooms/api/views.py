from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response

from rooms.api.serializers import RoomSerializer, RoomDetailsSerializer
from rooms.models import Room


# ViewSet for the model Room
class RoomViewSet(ModelViewSet):
    """ViewSet to model Room"""
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = (DjangoModelPermissions, IsAuthenticated)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RoomDetailsSerializer

        return self.serializer_class

    def destroy(self, request, *args, **kwargs):
        """Added validation to know if the room is not reserved for an event."""
        instance = self.get_object()
        if instance.is_reserved():
            raise ValidationError(_("This room is reserved for an event. Check."))
        else:
            self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


