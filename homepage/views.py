from django.shortcuts import render
from administrator.models import Country, Trip, Continent, City
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from django.utils.dateparse import parse_date
from django.views.generic import ListView
from homepage.forms import FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class All(ListView):
    queryset = Trip.objects.all()
    template_name = "homepage/home.html"
    context_object_name = "trips"
    paginate_by = 4


class FeedbackFormView(FormView):
    template_name = "homepage/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "homepage/success.html"


@csrf_exempt
def get_stripe_pubkey(request):
    if request.method == "GET":
        pub_key = settings.STRIPE_PUBLISHABLE_KEY
        return JsonResponse({"publicKey": pub_key})


def home(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    trips = Trip.objects.filter(
        Q(city_to_where__country__continent__name__icontains=q)
        | Q(city_from_where__country__continent__name__icontains=q)
        | Q(city_to_where__country__name__icontains=q)
        | Q(city_from_where__country__name__icontains=q)
        | Q(city_from_where__name__icontains=q)
        | Q(city_to_where__name__icontains=q)
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


# Nope. Django filters operate at the database level, generating SQL. To filter based on Python
# properties, you have to load the object into Python to evaluate the property
# cant use properties in queryset filter django
def interval_time(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    q1 = request.GET.get("q1") if request.GET.get("q1") is not None else ""
    trips_objects = Trip.objects.all()
    trips = [
        trip
        for trip in trips_objects
        if trip.date_departure > parse_date(q) and trip.date_return < parse_date(q1)
    ]

    context = {
        "trips": trips,
    }
    return render(request, "homepage/home.html", context)
