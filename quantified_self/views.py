from django.views.generic import ListView, DetailView

from quantified_self.models import IntervalEvent, IntCountEvent


class IntervalEventList(ListView):
    model = IntervalEvent
    template_name = "quantified_self/interval_list.html"


class IntCountEventList(ListView):
    model = IntCountEvent
    template_name = "quantified_self/integer_count_list.html"


class IntervalEventDetail(DetailView):
    model = IntervalEvent
    slug_url_kwarg = "uuid"
    slug_field = "uuid"
    template_name = "quantified_self/interval_detail.html"


class IntCountEventDetail(DetailView):
    model = IntCountEvent
    slug_url_kwarg = "uuid"
    slug_field = "uuid"
    template_name = "quantified_self/integer_count_detail.html"
