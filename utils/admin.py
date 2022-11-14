from django.contrib.auth.models import Permission
from django.contrib.gis import admin


class BaseAdmin(admin.ModelAdmin):
    """Generic models for standard empty fields"""
    empty_value_display = '---'


class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    fields = ['name', 'content_type', 'codename']

admin.site.register(Permission, PermissionAdmin)