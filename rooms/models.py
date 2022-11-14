from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from utils.models import AbstractDates

User = get_user_model()


class Room(AbstractDates):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    capacity = models.PositiveIntegerField(verbose_name=_('Capacity'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Room")
        verbose_name_plural = _("Rooms")
        ordering = ("created_at",)

    def is_reserved(self):
        """Method to determine which room is reserved for an event"""
        return True if hasattr(self, "event") else False
