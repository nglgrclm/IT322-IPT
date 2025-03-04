from django.urls import path
from .views import (
    LocationListCreateAPIView, LocationRetrieveUpdateDestroyAPIView,
    VehicleListCreateAPIView, VehicleRetrieveUpdateDestroyAPIView,
    BookingListCreateAPIView, BookingRetrieveUpdateDestroyAPIView,
    PaymentListCreateAPIView, PaymentRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('locations/', LocationListCreateAPIView.as_view(), name='list-create-location'),
    path('locations/<int:pk>/', LocationRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-location'),
    path('vehicles/', VehicleListCreateAPIView.as_view(), name='list-create-vehicle'),
    path('vehicles/<int:pk>/', VehicleRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-vehicle'),
    path('bookings/', BookingListCreateAPIView.as_view(), name='list-create-booking'),
    path('bookings/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-booking'),
    path('payments/', PaymentListCreateAPIView.as_view(), name='list-create-payment'),
    path('payments/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='retrieve-update-destroy-payment'),
]
