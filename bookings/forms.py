from django import forms
from .models import Booking
PACKAGE_CHOICES = [
    ("Wedding Photography", "Wedding Photography"),
    ("Portrait Session", "Portrait Session"),
    ("Birthday & Events", "Birthday & Events"),
    ("Graduation", "Graduation"),
    ("Corporate Event", "Corporate Event"),
    ("Family Photoshoot", "Family Photoshoot"),
]
class BookingForm(forms.ModelForm):
    package = forms.ChoiceField(
        choices=PACKAGE_CHOICES
    )
    class Meta:
        model = Booking
        fields = [
            "name",
            "email",
            "phone",
            "package",
            "date",
            "message",
        ]
        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Full Name"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email Address"
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "Phone Number"
            }),
            "date": forms.DateInput(attrs={
                "type": "date"
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Tell us about your event...",
                "rows": 5
            }),
        }