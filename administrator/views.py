from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
import stripe
from django.http import JsonResponse, HttpResponseRedirect
from django.utils import timezone

# from django.contrib.auth.decorators import login_required, permission_required

from administrator.forms import (
    AirportForm,
    CityForm,
    ContinentForm,
    CountryForm,
    HotelForm,
    PostForm,
    TripModelForm,
)
from .models import (
    Airport,
    City,
    Continent,
    Country,
    Hotel,
    Post,
    PurchaseOfATrip,
    Trip,
)

from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    DetailView,
    UpdateView,
)


@login_required
def like_trip(request, pk):
    trip = get_object_or_404(Trip, id=request.POST.get("trip_id"))
    trip.liked.add(request.user)
    return HttpResponseRedirect(reverse("trip-detail", args=[str(pk)]))


# BASE TEMPLATE OF ADMINISTRATOR FIELD
def administrator(request):
    return render(request, "administrator/index.html")


# CRUD FOR CONTINENT/LOCATION
@permission_required("continents.addcontinent")
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
@permission_required("countries.addcountry")
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
@permission_required("cities.addcity")
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
@permission_required("hotels.addhotel")
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
@permission_required("trips.addtrip")
def add_trip(request):
    if request.method == "POST":
        form = TripModelForm(request.POST, request.FILES)
        if form.is_valid():
            trip = form.save()
            messages.info(request, "Trip saved successfully")
            return redirect(trip, permanent=False)
    else:
        form = TripModelForm()
    return render(request, "administrator/trips/trip_add.html", context={"form": form})


@permission_required("trips.deletetrip")
def delete_trip(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        trip.delete()
        return redirect("trips-list")
    return render(
        request, "administrator/trips/trip_delete.html", context={"trip": trip}
    )


@login_required
def write_post(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.trip = trip
            post.user = request.user
            post.save()
            return redirect("trip-detail", pk=trip.pk)
    else:
        form = PostForm()
    return render(
        request,
        "administrator/post_form.html",
        context={
            "form": form,
            "trip": trip,
        },
    )


def get_trip_detail(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    qs = Post.objects.all()

    purchases = trip.purchases.all()
    revenue = sum(
        trip.price_for_adult * purchase.quantity_a
        + trip.price_for_child * purchase.quantity_ch
        for purchase in purchases
    )
    """    if trip.date_departure < date.today():
        trip.delete()
        return redirect("trips-list") 
        delete a trip from available trips"""

    context = {"qs": qs, "trip": trip, "revenue": revenue}
    return render(request, "administrator/trips/trip_detail.html", context)


def get_trips_list(request):
    trips = Trip.objects.all()
    return render(
        request,
        "administrator/trips/trips_list.html",
        context={
            "trips": trips,
        },
    )


class TripListView(ListView):
    queryset = Trip.objects.all()
    template_name = "administrator/trips/trips_list.html"
    context_object_name = "trips"
    paginate_by = 6


class TripUpdateView(UpdateView):
    model = Trip
    form_class = TripModelForm
    template_name = "administrator/trips/trip_add.html"


@csrf_exempt
@login_required
def purchase_trips(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)

    quantity_a = int(request.GET.get("quantity_a"))
    quantity_ch = int(request.GET.get("quantity_ch"))
    amount = (
        trip.price_for_adult * quantity_a * 100
        + trip.price_for_child * quantity_ch * 100
    ) // quantity_ch
    if (
        1
        > trip.remaining_places_adults  # per aq kohe sa ka ende vende per nje te rritur
    ):
        print("canot buy")
        return JsonResponse({"error": "No more trips available"}, status=400)

    if request.method == "GET":
        domain_url = "http://localhost:8000/"
        stripe.api_key = settings.STRIPE_SECRET_KEY
        success_url = (
            domain_url
            + "payments/success?session_id={CHECKOUT_SESSION_ID}"
            + f"&trip_id={trip.pk}&quantity_a={quantity_a}&quantity_ch={quantity_ch}"
        )
        try:
            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set
            # as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=success_url,
                cancel_url=domain_url + "payments/cancelled/",
                payment_method_types=["card"],
                mode="payment",
                line_items=[
                    {
                        "price_data": {
                            "currency": "eur",
                            "unit_amount": amount,
                            "product_data": {
                                "name": trip.city_to_where,
                                "description": trip.hotel_to_where,
                            },
                        },
                        "quantity": quantity_a,
                        "quantity": quantity_ch,
                    }
                ],
            )
            return JsonResponse({"sessionId": checkout_session["id"]})
        except Exception as e:
            return JsonResponse({"error": str(e)})


def payment_success(request):
    trip_id = request.GET.get("trip_id")
    if trip_id is not None:
        pk = int(trip_id)
        quantity_a = int(request.GET.get("quantity_a"))
        quantity_ch = int(request.GET.get("quantity_ch"))
        trip = Trip.objects.get(pk=pk)
        PurchaseOfATrip.objects.create(
            trip=trip,
            quantity_a=quantity_a,
            quantity_ch=quantity_ch,
            purchased_on=timezone.now(),
        )
    return render(request, "administrator/payment_success.html")


def payment_cancel(request):
    return render(request, "administrator/payment_cancelled.html")

