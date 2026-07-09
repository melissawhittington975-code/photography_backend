from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = [
            'full_name',
            'email',
            'phone',
            'package',
            'event_date',
            'event_time',
            'location',
            'guests',
            'budget',
            'message',
        ]

        widgets = {
            'event_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),

            'event_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),

            'message': forms.Textarea(attrs={
                'rows': 5,
                'class': 'form-control',
                'placeholder': 'Tell us about your event...'
            }),
        }