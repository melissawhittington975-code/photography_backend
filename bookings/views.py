from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Gallery, Booking


def home(request):
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("booking_success")

    gallery_images = Gallery.objects.all()[:6]
    total_bookings = Booking.objects.count()
    total_photos = Gallery.objects.count()

    context = {
        "form": form,
        "gallery_images": gallery_images,
        "total_bookings": total_bookings,
        "total_photos": total_photos,
    }

    return render(request, "bookings/home.html", context)


def about(request):
    return render(request, "bookings/about.html")


def services(request):
    return render(request, "bookings/services.html")


def gallery(request):
    gallery_images = Gallery.objects.all()

    return render(
        request,
        "bookings/gallery.html",
        {
            "gallery_images": gallery_images
        }
    )


def gallery_detail(request, id):
    photo = get_object_or_404(Gallery, id=id)

    return render(
        request,
        "bookings/gallery_detail.html",
        {
            "photo": photo
        }
    )


def booking(request):
    form = BookingForm()

    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("booking_success")

    return render(request, "bookings/booking.html", {"form": form})


def booking_success(request):
    return render(request, "bookings/booking_success.html")


def contact(request):
    return render(request, "bookings/contact.html")