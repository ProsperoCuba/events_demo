from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models


class AbstractDates(models.Model):
    """
    Abstract model for add creation and update times for records
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created Date"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated Date"))

    class Meta:
        abstract = True
