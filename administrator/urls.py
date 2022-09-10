from django.urls import path
from . import views

urlpatterns = [
    path("administrator/location/", views.index, name="location"),

    path("administrator/trips/", views.get_trips_list, name="trips-list"),
    path("administrator/trips/add/", views.add_trip, name="add-trip"),
    path("administrator/trips/<int:pk>/delete/", views.delete_trip, name="delete-trip"),
    path("administrator/trips/<int:pk>", views.get_trip_detail, name="trip-detail"),
    path("administrator/trips/<int:pk>/edit/", views.TripUpdateView.as_view(), name="trip-edit"),

    path(
        "administrator/location/continents",
        views.get_continents_list,
        name="continents-list",
    ),
    path(
        "administrator/location/continents/add/",
        views.add_continent,
        name="continent-add",
    ),
    path(
        "administrator/location/continents/<int:pk>/",
        views.get_continent_detail,
        name="continent-detail",
    ),
    path(
        "administrator/location/continents/<int:pk>/delete/",
        views.ContinentDeleteView.as_view(),
        name="continent-delete",
    ),
    path(
        "administrator/location/continents/<int:pk>/edit/",
        views.ContinentUpdateView.as_view(),
        name="continent-edit",
    ),


    path(
        "administrator/location/countries/",
        views.get_countries_list,
        name="countries-list",
    ),
    path("administrator/location/countries/add", views.add_country, name="country-add"),
    path(
        "administrator/location/countries/<int:pk>/",
        views.get_country_detail,
        name="country-detail",
    ),
    path(
        "administrator/location/countries/<int:pk>/delete/",
        views.CountryDeleteView.as_view(),
        name="country-delete",
    ),
    path(
        "administrator/location/countries/<int:pk>/edit/",
        views.CountryUpdateView.as_view(),
        name="country-edit",
    ),


    path("administrator/location/cities/", views.get_cities_list, name="cities-list"),
    path("administrator/location/cities/add", views.add_city, name="city-add"),
    path(
        "administrator/location/cities/<int:pk>/",
        views.get_city_detail,
        name="city-detail",
    ),
    path("administrator/location/cities/<int:pk>/delete", views.delete_city, name="delete-city"),
    path(
        "administrator/location/cities/<int:pk>/edit/",
        views.CityUpdateView.as_view(),
        name="city-edit",
    ),


    path(
        "administrator/location/airports/",
        views.AirportListView.as_view(),
        name="airports-list",
    ),
    path(
        "administrator/location/airports/add/",
        views.AirportCreateView.as_view(),
        name="airport-add",
    ),
    path(
        "administrator/location/airports/<int:pk>",
        views.AirportDetailView.as_view(),
        name="airport-detail",
    ),
    path(
        "administrator/location/airports/<int:pk>/delete/",
        views.AirportDeleteView.as_view(),
        name="airport-delete",
    ),
    path(
        "administrator/location/airports/<int:pk>/edit/",
        views.AirportUpdateView.as_view(),
        name="airport-edit",
    ),


    path(
        "administrator/hotels/",
        views.HotelListView.as_view(),
        name="hotels-list",
    ),
    path(
        "administrator/hotels/add/",
        views.add_hotel,
        name="add-hotel",
    ),
    path(
        "administrator/hotels/<int:pk>",
        views.HotelDetailView.as_view(),
        name="hotel-detail",
    ),
    path(
        "administrator/hotels/<int:pk>/delete/",
        views.HotelDeleteView.as_view(),
        name="hotel-delete",
    ),
    path(
        "administrator/hotels/<int:pk>/edit/",
        views.HotelUpdateView.as_view(),
        name="hotel-edit",
    ),
    path("administrator/purchases/", views.get_list_of_trips_to_purchase, name="list-of-trips-to-purchase"),
    path("administrator/purchases/<int:pk>/", views.purchase_trip, name="purchase-form"),
    path("administrator/purchases/all/", views.get_list_of_purchases, name="list-of-purchases"),
]
