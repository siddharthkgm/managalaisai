from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Booking
from .forms import BookingForm
from .utils import send_whatsapp_notification

class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/booking_form.html'
    success_url = reverse_lazy('my_bookings')

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        # Send Notification
        send_whatsapp_notification(self.object)
        return response
    
    def get_initial(self):
        initial = super().get_initial()
        if 'function_type' in self.request.GET:
            initial['function_type'] = self.request.GET.get('function_type')
        return initial

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-created_at')
