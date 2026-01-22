from django.views.generic import ListView
from events.models import FunctionType

class HomeView(ListView):
    model = FunctionType
    template_name = 'home.html'
    context_object_name = 'function_types'
