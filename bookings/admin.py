from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'function_type', 'venue_name', 'date', 'time', 'status')
    list_filter = ('status', 'date', 'function_type')
    search_fields = ('user__username', 'user__email', 'venue_name')
