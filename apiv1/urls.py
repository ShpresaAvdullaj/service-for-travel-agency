from django.urls import path
from apiv1 import views

urlpatterns = [
    path("trips/", views.TripListCreateView.as_view()),
    path("trips/<int:pk>/", views.TripDetailUpdateDeleteView.as_view()),
]