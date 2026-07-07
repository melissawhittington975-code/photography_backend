from django.contrib import admin
from django.urls import path
from bookings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('booking/', views.booking, name='booking'),
]