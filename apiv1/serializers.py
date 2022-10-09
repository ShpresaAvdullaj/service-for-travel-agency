from rest_framework import serializers
from administrator.models import Trip


class TripSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    city_from_where = serializers.CharField()
    city_to_where = serializers.CharField()
    airport_from_where = serializers.CharField()
    airport_to_where = serializers.CharField()
    hotel_to_where = serializers.CharField()
    date_of_departure = serializers.DateTimeField()
    date_of_return = serializers.DateTimeField()
    price_for_adult = serializers.IntegerField()
    price_for_child = serializers.IntegerField()
    number_of_places_per_adult = serializers.IntegerField()
    number_of_places_per_child = serializers.IntegerField()
    type = serializers.CharField()
    promoted = serializers.BooleanField()


"""
this method is to validate the input data while using api pages
def validate_dates(self, data):
        if (data['date_of_departure'] > data["date_of_return"]):
            raise serializers.ValidationError(
                "Client should have some holiday. Please enter the correct date!!"
            )
        return data
"""


class TripModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"
