# hotel_reservation_system/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservations/', include('reservations.urls')),
]