from django.shortcuts import render
from .forms import BookingForm
from .models import Gallery


def home(request):
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            form = BookingForm()

    gallery_images = Gallery.objects.all()[:6]

    return render(request, "bookings/home.html", {
        "form": form,
        "gallery_images": gallery_images,
    })


def about(request):
    return render(request, "bookings/about.html")


def gallery(request):
    gallery_images = Gallery.objects.all()

    return render(request, "bookings/gallery.html", {
        "gallery_images": gallery_images,
    })


def booking(request):

    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            form = BookingForm()

    return render(request, "bookings/booking.html", {
        "form": form,
    })


def contact(request):
    return render(request, "bookings/contact.html")


def services(request):
    return render(request, "bookings/services.html")