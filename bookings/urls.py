from django.urls import path
from .views import BookingCreateView, BookingListView

urlpatterns = [
    path('book/', BookingCreateView.as_view(), name='book_function'),
    path('my-bookings/', BookingListView.as_view(), name='my_bookings'),
]
