from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from core.enums import EventType
from rooms.models import Room
from utils.models import AbstractDates

User = get_user_model()


class Event(AbstractDates):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    room = models.OneToOneField(Room, verbose_name=_('Room'), on_delete=models.CASCADE, related_name="event")
    type = models.CharField(verbose_name=_('Type'), max_length=7, choices=EventType.choices, default=EventType.public)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ("created_at",)

    @property
    def is_private(self):
        return self.type == EventType.private

    @property
    def is_public(self):
        return self.type == EventType.public

    @property
    def is_available(self):
        return self.room.capacity > 0

