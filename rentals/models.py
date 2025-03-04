from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"
        ordering = ["name"]
        db_table = "location"

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    vehicle_type = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="vehicles")

    def __str__(self):
        return f"{self.name} ({self.vehicle_type})"

    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
        ordering = ["name"]
        db_table = "vehicle"

class Booking(models.Model):
    STATUS_CHOICES = [
        ('successful', 'Successful'),
        ('failed', 'Failed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="bookings")
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="bookings")
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='successful')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Booking {self.id} - {self.user.username} - {self.vehicle.name}"

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-date"]
        db_table = "booking"

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name="payment")
    status = models.CharField(max_length=20, choices=[('successful', 'Successful'), ('failed', 'Failed')])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Booking {self.booking.id} - {self.status}"

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ["-transaction_date"]
        db_table = "payment"

        

