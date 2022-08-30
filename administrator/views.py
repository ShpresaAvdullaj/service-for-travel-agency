from django.shortcuts import render

from administrator.forms import CityForm, ContinentForm, CountryForm, TripForm
from .models import City, Continent, Country, Trip
from django.shortcuts import redirect, get_object_or_404

from django.views.generic import CreateView


def index(request):
    return render(request, "administrator/index_location.html")


def get_continent_detail(request, pk):
    continent = get_object_or_404(Continent, pk=pk)
    return render(
        request,
        "administrator/location/continent_detail.html",
        context={"continent": continent},
    )


def get_country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(
        request,
        "administrator/location/country_detail.html",
        context={"country": country},
    )


def get_city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(
        request,
        "administrator/location/city_detail.html",
        context={"city": city},
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


def get_countries_list(request):
    countries = Country.objects.all()
    return render(
        request,
        "administrator/location/countries_list.html",
        context={
            "countries": countries,
        },
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


def get_continents_list(request):
    continents = Continent.objects.all()
    return render(
        request,
        "administrator/location/continents_list.html",
        context={
            "continents": continents,
        },
    )


def add_trip(request):
    if request.method == "POST":
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            trip = form.save()
            return redirect("trip-detail", pk=trip.pk)
    else:
        form = TripForm()
    return render(request, "administrator/trips/trip_add.html", context={"form": form})


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


class ContinentCreateView(CreateView):
    model = Continent
    fields = ["name"]
