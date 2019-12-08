from django.views.generic import ListView
from django.shortcuts import render

from quantified_self.models import IntervalEvent


class IntervalEventList(ListView):
    model = IntervalEvent
    template_name = "quantified_self/interval_event_list.html"

def index(request):
    """
    Index view
    """
    return render(request, 'quantified_self/index.html', {})
