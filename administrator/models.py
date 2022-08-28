from django.db import models
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation


class Continent(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "continents"

    def __str__(self):
        return f"{self.name}"


class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(
        Continent, verbose_name=("continent"), on_delete=models.CASCADE
    )

    class Meta:
        db_table = "countries"

    def __str__(self):
        return f"{self.name}-{self.continent}"


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(
        Country, verbose_name=("country"), on_delete=models.CASCADE
    )

    class Meta:
        db_table = "cities"

    def __str__(self):
        return f"{self.name}-{self.country}"


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    standart = GenericRelation(Rating)
    description = models.TextField(null=True)
    photo = models.ImageField(null=True, upload_to="hotels")
    city = models.ForeignKey(
        City, verbose_name=("city"), on_delete=models.CASCADE
    )

    class Meta:
        db_table = "hotels"

    def __str__(self):
        return f"{self.name}-{self.standart}-{self.description}-{self.photo}-{self.city}"


class Airport(models.Model):
    name = models.CharField(max_length=70)
    city = models.ForeignKey(
        City, verbose_name=("city"), on_delete=models.CASCADE
    )

    class Meta:
        db_table = "airports"

    def __str__(self):
        return f"{self.name}-{self.city}"


class Trip(models.Model):
    TYPES = [
        (" BB ", "bed & breakfast"),
        (" HB ", "half board"),
        (" FB ", "full board"),
        (" AI ", "all inclusive")
    ]

    city_from_where = models.ForeignKey(
        City, verbose_name=("city from where"), on_delete=models.CASCADE,
        related_name="city from where +")
    Airport_from_where = models.ForeignKey(
        Airport, verbose_name=("airport from where"), on_delete=models.CASCADE,
        related_name="airport from where +")
    city_to_where = models.ForeignKey(
        City, verbose_name=("city to where"), on_delete=models.CASCADE,
        related_name="city to where +")
    airport_to_where = models.ForeignKey(
        Airport, verbose_name=("airport to where"), on_delete=models.CASCADE,
        related_name="airport to where +")
    hotel_to_where = models.ForeignKey(
        City, verbose_name=("hotel to where"), on_delete=models.CASCADE,
        related_name="hotel to where +")
    date_of_departure = models.DateField(null=True)
    date_of_return = models.DateField(null=True)
    number_of_days = models.IntegerField()
    type = models.CharField(max_length=10, choices=TYPES)
    price_for_adult = models.IntegerField()
    price_for_child = models.IntegerField()
    promoted = models.BooleanField(default=False)
    number_of_places_per_adult = models.IntegerField()
    number_of_places_per_child = models.IntegerField()

    class Meta:
        db_table = "trips"

    def __str__(self):
        return f"{self.from_where}-{self.to_where}-{self.date_of_departure}-{self.date_of_return}-{self.type}-{self.price_for_adult}-{self.price_for_child}-{self.number_of_places_per_adult}-{self.number_of_places_per_child}"


class PurchaseOfATrip(models.Model):

    number_of_adults = Trip.number_of_places_per_adult
    number_of_child = Trip.number_of_places_per_child
    price_for_adult = Trip.price_for_adult
    price_for_child = Trip.price_for_child

    trip = models.CharField(max_length=10)
    participant_details = models.CharField(max_length=100)
    amount = models.IntegerField()

    class Meta:
        db_table = "purchasesfortrip"

    def __str__(self):
        return f"Your trip {self.trip} {self.participant_details} costs {self.amount}"
