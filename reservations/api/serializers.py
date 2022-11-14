from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from reservations.models import Reservation

User = get_user_model()


class ReservationSerializer(serializers.ModelSerializer):
    """Serializer to model Reservations"""

    user = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())

    class Meta:
        model = Reservation
        fields = "__all__"

    def validate(self, attrs):
        event = attrs.get('event')
        if event.is_private:
            raise ValidationError({'event': _("This event is private")})
        elif not event.is_available:
            raise ValidationError({'event': _("There is no capacity for the event.")})

        return attrs


class ReservationDetailsSerializer(serializers.ModelSerializer):
    """Serializer to model Reservations"""
    user = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = "__all__"

    def get_user(self, obj):
        from users.api.serializers import UserXsSerializer
        return UserXsSerializer(obj.user).data if obj.user else None

    def get_event(self, obj):
        from events.api.serializers import EventDetailsSerializer
        return EventDetailsSerializer(obj.event).data if obj.event else None