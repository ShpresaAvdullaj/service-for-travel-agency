from django import forms
from .models import City, Continent, Country, Hotel, Trip, PurchaseOfATrip, Airport


class ContinentForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields = "__all__"


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = "__all__"


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = "__all__"


class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = "__all__"


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ["name", "standart", "description", "photo", "city"]


def _get_cities():
    return [("", "-- City --")] + [(city.pk, str(city)) for city in City.objects.all()]


def _to_city(val):
    pk = int(val)
    return City.objects.get(pk=pk)


def _get_airports():
    return [("", "-- Airport --")] + [
        (airport.pk, str(airport)) for airport in Airport.objects.all()
    ]


def _to_hotel(val):
    pk = int(val)
    return Hotel.objects.get(pk=pk)


def _get_hotels():
    return [("", "-- Hotel --")] + [
        (hotel.pk, str(hotel)) for hotel in Hotel.objects.all()
    ]


def _to_airport(val):
    pk = int(val)
    return Airport.objects.get(pk=pk)


TYPES = [
    (" BB ", "bed & breakfast"),
    (" HB ", "half board"),
    (" FB ", "full board"),
    (" AI ", "all inclusive"),
]


class TripForm(forms.Form):

    city_from_where = forms.TypedChoiceField(
        required=True, coerce=_to_city, choices=_get_cities
    )
    airport_from_where = forms.TypedChoiceField(
        required=True, coerce=_to_airport, choices=_get_airports
    )
    city_to_where = forms.TypedChoiceField(
        required=True, coerce=_to_city, choices=_get_cities
    )
    airport_to_where = forms.TypedChoiceField(
        required=True, coerce=_to_airport, choices=_get_airports
    )
    hotel_to_where = forms.TypedChoiceField(
        required=True, coerce=_to_hotel, choices=_get_hotels
    )
    date_of_departure = forms.DateField()
    date_of_return = forms.DateField()
    number_of_days = forms.IntegerField()
    type = forms.ChoiceField(required=True, choices=TYPES)
    price_for_adult = forms.IntegerField()
    price_for_child = forms.IntegerField()
    promoted = forms.BooleanField()
    number_of_places_per_adult = forms.IntegerField()
    number_of_places_per_child = forms.IntegerField()


class TripModelForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            "city_from_where",
            "city_to_where",
            "airport_from_where",
            "airport_to_where",
            "hotel_to_where",
            "date_of_departure",
            "date_of_return",
            "number_of_days",
            "price_for_adult",
            "price_for_child",
            "number_of_places_per_adult",
            "number_of_places_per_child",
            "type",
            "promoted",
        ]


class PurchaseOfATripForm(forms.ModelForm):
    class Meta:
        model = PurchaseOfATrip
        fields = "__all__"
