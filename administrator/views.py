from django.shortcuts import render

from administrator.forms import ContinentForm, TripForm
from .models import Continent, Trip
from django.shortcuts import redirect, get_object_or_404

from django.views.generic import CreateView


def get_continent_detail(request, pk):
    continent = get_object_or_404(Continent, pk=pk)
    return render(
        request,
        "administrator/continents/continent_detail.html",
        context={"continent": continent},
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


def get_continents_list(request):
    continents = Continent.objects.all()
    return render(
        request,
        "administrator/continents/continents_list.html",
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
        request, "administrator/continents/continent_add.html", context={"form": form}
    )


class ContinentCreateView(CreateView):
    model = Continent
    fields = ["name"]
