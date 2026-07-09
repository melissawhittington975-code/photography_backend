from django.db import models


class Booking(models.Model):
    PACKAGE_CHOICES = [
        ("Wedding", "Wedding"),
        ("Portrait", "Portrait"),
        ("Event", "Event"),
        ("Graduation", "Graduation"),
        ("Family", "Family"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    package = models.CharField(
        max_length=20,
        choices=PACKAGE_CHOICES
    )

    event_date = models.DateField()
    event_time = models.TimeField()

    location = models.CharField(max_length=200)

    guests = models.PositiveIntegerField()

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.full_name


class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ("Wedding", "Wedding"),
        ("Portrait", "Portrait"),
        ("Event", "Event"),
        ("Graduation", "Graduation"),
        ("Family", "Family"),
    ]

    title = models.CharField(max_length=100)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(upload_to="gallery/")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title