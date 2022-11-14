from django.http import QueryDict
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from reservations.api.serializers import ReservationSerializer, ReservationDetailsSerializer
from reservations.models import Reservation


class ReservationViewSet(ModelViewSet):
    """ViewSet to model Reservation"""
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = (DjangoModelPermissions, IsAuthenticated)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReservationDetailsSerializer

        return self.serializer_class

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return self.queryset.filter(user=user)

        return self.queryset

    def create(self, request, *args, **kwargs):
        data = request.data.dict() if isinstance(request.data, QueryDict) else request.data
        auth_user = request.user

        if auth_user.is_superuser:
            if not data.get('user', None):
                raise ValidationError({'user': _("This field is required")})

        else:
            data['user'] = auth_user.id

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        # Validating that the user does not book twice for the same event
        if Reservation.objects.filter(user_id=data['user'], event_id=data['event']).exists():
            raise ValidationError({'event': _("Already booked for this event.")})

        self.perform_create(serializer)

        # Validating that when a reservation is created, the capacity of the event room is decremented
        serializer.instance.event.room.capacity -= 1
        serializer.instance.event.room.save()
        r_serializer = ReservationDetailsSerializer(instance=serializer.instance)
        headers = self.get_success_headers(r_serializer.data)
        return Response(r_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        """Validating that when eliminated, the capacity of the event room is increased."""
        instance = self.get_object()
        instance.event.room.capacity += 1
        instance.event.room.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)




