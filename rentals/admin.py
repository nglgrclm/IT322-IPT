from django.contrib import admin
from .models import Booking, Location, Payment, Vehicle

# Register your models here.

admin.site.register(Booking)
admin.site.register(Location)
admin.site.register(Payment)
admin.site.register(Vehicle)