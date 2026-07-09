from django.contrib import admin
from .models import Booking, Gallery


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        "full_name",
        "package",
        "status",
        "event_date",
        "event_time",
        "phone",
        "location",
        "created_at",
    )

    list_filter = (
        "status",
        "package",
        "event_date",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "location",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 15


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "created_at",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "title",
        "category",
    )

    ordering = (
        "-created_at",
    )

    list_per_page = 20