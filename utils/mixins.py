from django.contrib.admin import ModelAdmin
from django.db import models
from rest_framework import filters
from django_filters import rest_framework as django_filters

# Common backend search filter for viewsets
SEARCH_BACKEND_FILTER = (
    django_filters.DjangoFilterBackend,
    filters.SearchFilter,
)


class BaseAdmin(ModelAdmin):
    """Base Events Admin model for define empty default values"""
    empty_value_display = '---'


class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def get_prep_value(self, value):
        value = super(LowercaseEmailField, self).get_prep_value(value)
        if isinstance(value, str):
            return value.lower()
        return value
