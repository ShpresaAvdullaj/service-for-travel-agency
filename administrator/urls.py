from django.urls import path
from . import views

urlpatterns = [
    path("administrator/trips/", views.get_trips_list, name="trips-list"),
    path("administrator/trips/add/", views.add_trip, name="add-trip"),
    path("administrator/location/", views.index, name="location"),
    path(
        "administrator/location/continents", views.get_continents_list, name="continents-list"
    ),
    path("administrator/location/continents/add/", views.add_continent, name="continent-add"),
    path(
        "administrator/location/continents/<int:pk>/",
        views.get_continent_detail,
        name="continent-detail",
    ),
    path(
        "administrator/location/countries/", views.get_countries_list, name="countries-list"
    ),
    path("administrator/location/countries/add", views.add_country, name="country-add"),
    path(
        "administrator/location/countries/<int:pk>/",
        views.get_country_detail,
        name="country-detail",
    ),
    path(
        "administrator/location/cities/", views.get_cities_list, name="cities-list"
    ),
    path("administrator/location/cities/add", views.add_city, name="city-add"),
    path(
        "administrator/location/cities/<int:pk>/",
        views.get_city_detail,
        name="city-detail",
    ),
]
