from django.shortcuts import render
from administrator.models import Country, Trip, Continent, City
from django.db.models import Q


def home(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    trips = Trip.objects.filter(
        Q(city_to_where__country__continent__name__icontains=q)
        | Q(city_to_where__country__name__icontains=q)
    )

    continents = Continent.objects.all()
    countries = Country.objects.all()
    cities = City.objects.all()
    # trip_reserved_count = trip.count()

    context = {
        "trips": trips,
        "continents": continents,
        "cities": cities,
        "countries": countries,
    }
    return render(request, "homepage/home.html", context)
