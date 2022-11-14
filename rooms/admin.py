from django.contrib import admin

from rooms.models import Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "capacity", "created_at")
    search_fields = ["name"]


admin.site.register(Room, RoomAdmin)
