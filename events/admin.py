from django.contrib import admin

from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "room", "type", "created_at")
    search_fields = ["name", "room__name"]


admin.site.register(Event, EventAdmin)
