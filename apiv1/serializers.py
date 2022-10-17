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


class TripModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = "__all__"

    def validate_number_of_places_per_adult(self, value):
        if value >= 1:
            return value
        raise serializers.ValidationError("A trip can not start without an adult.")

    def validate(self, data):
        if data["date_of_departure"] >= data["date_of_return"]:
            raise serializers.ValidationError(
                "Date of departure can not be greater than date of return. Client should have some holidays."
            )
        return data
