from django.contrib.auth import get_user_model
from rest_framework import serializers

from events.models import Event

User = get_user_model()


class EventSerializer(serializers.ModelSerializer):
    """Serializer to model Events"""

    class Meta:
        model = Event
        fields = "__all__"


class EventDetailsSerializer(serializers.ModelSerializer):
    """Serializer to model Events"""

    room = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ("id", "name", "type", "room")

    def get_room(self, obj):
        from rooms.api.serializers import RoomDetailsSerializer
        return RoomDetailsSerializer(obj.room).data if obj.room else None
