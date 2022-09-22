from django.shortcuts import render
from administrator.models import Country, Trip, Continent, City, FilterDate
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings


@csrf_exempt
def get_stripe_pubkey(request):
    if request.method == "GET":
        pub_key = settings.STRIPE_PUBLISHABLE_KEY
        return JsonResponse({"publicKey": pub_key})


def home(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    trips = Trip.objects.filter(
        Q(city_to_where__country__continent__name__icontains=q)
        | Q(city_to_where__country__name__icontains=q)
        | Q(date_of_departure__icontains=q)
        | Q(type__icontains=q)
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


def type_inclusive(request):
    trips = Trip.objects.filter(Q(type__icontains="AI"))
    context = {
        "trips": trips,
    }
    return render(request, "homepage/home.html", context)


def type_half_broad(request):
    trips = Trip.objects.filter(Q(type__icontains="HB"))
    context = {
        "trips": trips,
    }
    return render(request, "homepage/home.html", context)


def type_full_broad(request):
    trips = Trip.objects.filter(Q(type__icontains="FB"))
    context = {
        "trips": trips,
    }
    return render(request, "homepage/home.html", context)


def type_bed_breakfast(request):
    trips = Trip.objects.filter(Q(type__icontains="BB"))
    context = {
        "trips": trips,
    }
    return render(request, "homepage/home.html", context)


def interval_time(request):
    filter_date = FilterDate()
    trip = Trip.objects.all()
    trips = [
        trip
        for tr in trip
        if filter_date.first_date
        < tr.date_of_departure.date()
        < filter_date.second_date
    ]
    context = {
        "trips": trips,
    }
    return render(request, "homepage/home.html", context)
