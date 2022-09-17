from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

from administrator.forms import (
    AirportForm,
    CityForm,
    ContinentForm,
    CountryForm,
    HotelForm,
    PurchaseOfATripForm,
    TripModelForm,
)
from .models import Airport, City, Continent, Country, Hotel, PurchaseOfATrip, Trip

from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
)


# BASE TEMPLATE OF ADMINISTRATOR FIELD
def index(request):
    return render(request, "administrator/index_location.html")


# CRUD FOR CONTINENT/LOCATION
def add_continent(request):
    if request.method == "POST":
        form = ContinentForm(request.POST, request.FILES)
        if form.is_valid():
            continent = form.save()
            return redirect("continent-detail", pk=continent.pk)
    else:
        form = ContinentForm()
    return render(
        request, "administrator/location/continent_add.html", context={"form": form}
    )


def get_continents_list(request):
    continents = Continent.objects.all()
    return render(
        request,
        "administrator/location/continents_list.html",
        context={
            "continents": continents,
        },
    )


def get_continent_detail(request, pk):
    continent = get_object_or_404(Continent, pk=pk)
    return render(
        request,
        "administrator/location/continent_detail.html",
        context={"continent": continent},
    )


class ContinentDeleteView(DeleteView):
    model = Continent
    template_name = "administrator/location/continent_delete.html"
    success_url = reverse_lazy("continents-list")


class ContinentUpdateView(UpdateView):
    model = Continent
    form_class = ContinentForm
    template_name = "administrator/location/continent_add.html"


# CRUD FOR COUNTRY/LOCATION
def add_country(request):
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            country = form.save()
            return redirect("country-detail", pk=country.pk)
    else:
        form = CountryForm()
    return render(
        request, "administrator/location/country_add.html", context={"form": form}
    )


def get_countries_list(request):
    countries = Country.objects.all()
    return render(
        request,
        "administrator/location/countries_list.html",
        context={
            "countries": countries,
        },
    )


def get_country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(
        request,
        "administrator/location/country_detail.html",
        context={"country": country},
    )


class CountryDeleteView(DeleteView):
    model = Country
    template_name = "administrator/location/country_delete.html"
    success_url = reverse_lazy("countries-list")


class CountryUpdateView(UpdateView):
    model = Country
    form_class = CountryForm
    template_name = "administrator/location/country_add.html"


# CRUD FOR CITY/LOCATION
def add_city(request):
    if request.method == "POST":
        form = CityForm(request.POST, request.FILES)
        if form.is_valid():
            city = form.save()
            return redirect("city-detail", pk=city.pk)
    else:
        form = CityForm()
    return render(
        request, "administrator/location/city_add.html", context={"form": form}
    )


def get_cities_list(request):
    cities = City.objects.all()
    return render(
        request,
        "administrator/location/cities_list.html",
        context={
            "cities": cities,
        },
    )


def delete_city(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == "POST":
        city.delete()
        return redirect("cities-list")
    return render(
        request, "administrator/location/city_delete.html", context={"city": city}
    )


def get_city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(
        request,
        "administrator/location/city_detail.html",
        context={"city": city},
    )


class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = "administrator/location/city_add.html"


# CRUD FOR AIRPORT/LOCATION
class AirportListView(ListView):
    queryset = Airport.objects.all()
    template_name = "administrator/location/airports_list.html"
    context_object_name = "airports"


class AirportCreateView(CreateView):
    model = Airport
    fields = ["name", "city"]
    template_name = "administrator/location/airport_add.html"


class AirportDetailView(DetailView):
    model = Airport
    template_name = "administrator/location/airport_detail.html"


class AirportDeleteView(DeleteView):
    model = Airport
    template_name = "administrator/location/airport_confirm_delete.html"
    success_url = reverse_lazy("airports-list")


class AirportUpdateView(UpdateView):
    model = Airport
    form_class = AirportForm
    template_name = "administrator/location/airport_add.html"


# CRUD FOR HOTELS
def add_hotel(request):
    if request.method == "POST":
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            hotel = form.save()
            return redirect("hotel-detail", pk=hotel.pk)
    else:
        form = HotelForm()
    return render(
        request, "administrator/hotels/hotel_add.html", context={"form": form}
    )


class HotelListView(ListView):
    queryset = Hotel.objects.all()
    template_name = "administrator/hotels/hotels_list.html"
    context_object_name = "hotels"


class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = "administrator/hotels/hotel_delete.html"
    success_url = reverse_lazy("hotels-list")


class HotelUpdateView(UpdateView):
    model = Hotel
    form_class = HotelForm
    template_name = "administrator/hotels/hotel_add.html"


class HotelDetailView(DetailView):
    model = Hotel
    template_name = "administrator/hotels/hotel_detail.html"


# CRUD FOR TRIPS
def add_trip(request):
    if request.method == "POST":
        form = TripModelForm(request.POST, request.FILES)
        if form.is_valid():
            trip = form.save()
            return redirect("trip-detail", pk=trip.pk)
    else:
        form = TripModelForm()
    return render(request, "administrator/trips/trip_add.html", context={"form": form})


def delete_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        trip.delete()
        return redirect("trips-list")
    return render(
        request, "administrator/trips/trip_delete.html", context={"trip": trip}
    )


def get_trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    purchases = trip.purchaseofatrip_set.all()

    revenue = sum(
        trip.price_for_adult * purchase.number_of_adults_participant
        for purchase in purchases
    )
    return render(
        request,
        "administrator/trips/trip_detail.html",
        context={"trip": trip, "revenue": revenue},
    )


def get_trips_list(request):
    trips = Trip.objects.all()
    return render(
        request,
        "administrator/trips/trips_list.html",
        context={
            "trips": trips,
        },
    )


class TripUpdateView(UpdateView):
    model = Trip
    form_class = TripModelForm
    template_name = "administrator/trips/trip_add.html"


# CRUD FOR PURCHASE OF A TRIP


def get_list_of_trips_to_purchase(request):
    trips = Trip.objects.all()
    return render(
        request,
        "administrator/purchases/list_of_trips_to_purchase.html",
        context={
            "trips": trips,
        },
    )


def purchase_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = PurchaseOfATripForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect("trip-detail", pk=trip.pk)
    else:
        form = PurchaseOfATripForm()
    return render(
        request,
        "administrator/purchases/purchase_form.html",
        context={
            "form": form,
            "trip": trip,
        },
    )


def get_list_of_purchases(request):
    purchases = PurchaseOfATrip.objects.all()
    return render(
        request,
        "administrator/purchases/list_of_purchases.html",
        context={
            "purchases": purchases,
        },
    )
