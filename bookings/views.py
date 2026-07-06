from django.shortcuts import render
from django.contrib import messages
from .forms import BookingForm

def home(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you! Your booking has been received. We'll contact you shortly."
            )
            form = BookingForm()
    else:
        form = BookingForm()

    return render(request, "bookings/home.html", {"form": form})