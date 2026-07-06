from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "phone",
        "package",
        "date",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "package",
    )

    list_filter = (
        "package",
        "date",
    )

    ordering = ("-date",)