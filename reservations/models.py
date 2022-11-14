from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from events.models import Event
from rooms.models import Room
from utils.models import AbstractDates

User = get_user_model()


class Reservation(AbstractDates):
    user = models.ForeignKey(User, verbose_name=_('Customer'), on_delete=models.CASCADE, related_name="reservation")
    event = models.ForeignKey(Event, verbose_name=_('Events'), on_delete=models.CASCADE, related_name="reservation")

    def __str__(self):
        return self.user.__str__()

    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")
        ordering = ("created_at",)


