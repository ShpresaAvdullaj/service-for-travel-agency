from django.urls import path

from . import views

urlpatterns = [
    path("promotions/", views.promoted_trips, name="promoted-trips"),
]