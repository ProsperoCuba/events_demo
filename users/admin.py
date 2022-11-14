from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as ContribUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(ContribUserAdmin):
    fieldsets = None

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

    list_display = (
        "id",
        "is_active",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "date_joined",
    )
    list_filter = ("is_active",)
    raw_id_fields = ("groups",)
