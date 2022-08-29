from django.urls import path
from . import views

urlpatterns = [
    path("administrator/trips/", views.get_trips_list, name="trips-list"),
    path("administrator/trips/add/", views.add_trip, name="add-trip"),
    path(
        "administrator/continents/", views.get_continents_list, name="continents-list"
    ),
    path("administrator/continents/add/", views.add_continent, name="continent-add"),
    path(
        "administrator/continents/<int:pk>/",
        views.get_continent_detail,
        name="continent-detail",
    ),
]
