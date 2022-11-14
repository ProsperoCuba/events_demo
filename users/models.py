from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from model_utils.models import SoftDeletableModel
from django.utils.translation import ugettext_lazy as _

from utils.mixins import LowercaseEmailField
from utils.models import AbstractDates


class User(AbstractUser, SoftDeletableModel):

    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        "user",
        max_length=150,
        help_text=_('150 characters or less. Only letters, digits and @/./+/-/_'),
        null=True,
        unique=True,
        validators=[username_validator],
    )
    email = LowercaseEmailField(verbose_name=_('Email'), unique=True)

    def __str__(self):
        return self.get_full_name_or_email

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ("-date_joined",)

    @property
    def get_full_name_or_email(self):
        if self.first_name and self.last_name:
            return self.get_full_name()
        return self.email

