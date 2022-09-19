from django.db import models
from django.urls import reverse
from django.db.models import Sum

from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation


class Continent(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "continents"

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("continent-detail", kwargs={"pk": self.pk})


class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(
        Continent, verbose_name=("continent"), on_delete=models.CASCADE
    )

    class Meta:
        db_table = "countries"

    def __str__(self):
        return f"{self.name}-{self.continent}"

    def get_absolute_url(self):
        return reverse("country-detail", kwargs={"pk": self.pk})


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country, verbose_name=("country"), on_delete=models.CASCADE
    )

    class Meta:
        db_table = "cities"

    def __str__(self):
        return f"{self.name}-{self.country}"

    def get_absolute_url(self):
        return reverse("city-detail", kwargs={"pk": self.pk})


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    standart = models.IntegerField(null=True)
    description = models.TextField(null=True)
    photo = models.ImageField(null=True, upload_to="hotels")
    city = models.ForeignKey(City, verbose_name=("city"), on_delete=models.CASCADE)

    class Meta:
        db_table = "hotels"

    def __str__(self):

        return (
            f"{self.name}-{self.standart}-{self.photo}-{self.city}"
        )

    def get_absolute_url(self):
        return reverse("hotel-detail", kwargs={"pk": self.pk})


class Airport(models.Model):
    name = models.CharField(max_length=70)
    city = models.ForeignKey(City, verbose_name=("city"), on_delete=models.CASCADE)

    class Meta:
        db_table = "airports"

    def __str__(self):
        return f"{self.name}-{self.city}"

    def get_absolute_url(self):
        return reverse("airport-detail", kwargs={"pk": self.pk})


class Trip(models.Model):
    TYPES = [
        (" BB ", "bed & breakfast"),
        (" HB ", "half board"),
        (" FB ", "full board"),
        (" AI ", "all inclusive"),
    ]

    city_from_where = models.ForeignKey(
        City,
        verbose_name=("city from where"),
        on_delete=models.CASCADE,
        related_name="city from where +",
    )
    city_to_where = models.ForeignKey(
        City,
        verbose_name=("city to where"),
        on_delete=models.CASCADE,
        related_name="city to where +",
    )
    airport_from_where = models.ForeignKey(
        Airport,
        verbose_name=("airport from where"),
        on_delete=models.CASCADE,
        related_name="airport from where +",
    )
    airport_to_where = models.ForeignKey(
        Airport,
        verbose_name=("airport to where"),
        on_delete=models.CASCADE,
        related_name="airport to where +",
    )
    hotel_to_where = models.ForeignKey(
        Hotel,
        verbose_name=("hotel to where"),
        on_delete=models.CASCADE,
        related_name="hotel to where +",
    )
    date_of_departure = models.DateField(null=True)
    date_of_return = models.DateField(null=True)
    number_of_days = models.IntegerField()
    price_for_adult = models.IntegerField(default=20)
    price_for_child = models.IntegerField(default=15)
    number_of_places_per_adult = models.IntegerField(default=0)
    number_of_places_per_child = models.IntegerField(default=0)
    type = models.CharField(max_length=10, choices=TYPES)
    promoted = models.BooleanField(default=False)

    class Meta:
        db_table = "trips"

    def __str__(self):
        return f"{self.city_to_where}-{self.date_of_departure}-{self.date_of_return}-{self.type}"

    def get_absolute_url(self):
        return reverse("trip-detail", kwargs={"pk": self.pk})

    @property
    def remaining_places_adults(self):
        reserved_for_adults = self.purchases.aggregate(Sum("quantity_a"))
        total = 0 if reserved_for_adults.get("quantity__sum") is None else reserved_for_adults.get("quantity__sum")
        return self.number_of_places_per_adult - total

    @property
    def remaining_places_child(self):
        reserved_for_child = self.purchases.aggregate(Sum("quantity_ch"))
        total = 0 if reserved_for_child.get("quantity__sum") is None else reserved_for_child.get("quantity__sum")
        return self.number_of_places_per_child - total


class PurchaseOfATrip(models.Model):
    trip = models.ForeignKey(Trip, related_name="purchases", verbose_name=("trip"), on_delete=models.CASCADE)
    quantity_a = models.IntegerField(default=1)
    quantity_ch = models.IntegerField(default=0)
    purchased_on = models.DateTimeField()

    class Meta:
        db_table = "purchases"

    def __str__(self):
        return f"Your trip{self.trip}{self.purchased_on}"





