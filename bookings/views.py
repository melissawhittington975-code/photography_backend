from django.shortcuts import render, redirect
from .forms import BookingForm
from .models import Booking

def home(request):
    return render(request, 'bookings/home.html')

def gallery(request):
    return render(request, 'bookings/gallery.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            # WhatsApp redirect (change number)
            phone = "2348167211192"
            message = f"New Booking: {booking.name}, {booking.service} on {booking.date}"
            whatsapp_url = f"https://wa.me/{phone}?text={message}"

            return redirect(whatsapp_url)

    else:
        form = BookingForm()

    return render(request, 'bookings/booking.html', {'form': form})