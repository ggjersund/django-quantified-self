from django.urls import path
from . views import IntervalEventList, index


app_name = 'quantified_self'


urlpatterns = [
    path('list/', IntervalEventList.as_view(), name="list"),
    path('index/', index, name="index"),
]
