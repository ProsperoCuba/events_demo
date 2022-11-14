from django.contrib.auth import get_user_model
from rest_framework import serializers

from rooms.models import Room

User = get_user_model()


class RoomSerializer(serializers.ModelSerializer):
    """Serializer to model Room"""

    class Meta:
        model = Room
        fields = "__all__"


class RoomDetailsSerializer(serializers.ModelSerializer):
    """Serializer to model Room"""

    class Meta:
        model = Room
        fields = ("id", "name", "capacity")
