from django.urls import path
from quantified_self import views

app_name = 'quantified_self'

urlpatterns = [
    path('intervals/', views.IntervalEventList.as_view(), name="interval-list"),
    path('intervals/<uuid:uuid>/', views.IntervalEventDetail.as_view(), name="interval-detail"),
    path('counts/', views.IntCountEventList.as_view(), name="count-list"),
    path('counts/<uuid:uuid>/', views.IntCountEventDetail.as_view(), name="count-detail")
]
