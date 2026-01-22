from django.db import models
from django.conf import settings
from events.models import FunctionType

class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    function_type = models.ForeignKey(FunctionType, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    phone = models.CharField(max_length=15, default="")
    venue_name = models.CharField(max_length=200, help_text="Enter the name of the venue")
    venue_address = models.TextField(help_text="Enter the address of the venue")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.function_type.name} on {self.date}"
