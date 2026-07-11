from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("gallery/", views.gallery, name="gallery"),
    path("gallery/<int:id>/", views.gallery_detail, name="gallery_detail"),
    path("booking/", views.booking, name="booking"),
    path("booking/success/", views.booking_success, name="booking_success"),
    path("contact/", views.contact, name="contact"),
]