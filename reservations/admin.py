from django.contrib import admin

from reservations.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ("user", "event", "created_at")
    search_fields = ["user__first_name", "user__last_name", "user__email", "event__name"]


admin.site.register(Reservation, ReservationAdmin)
