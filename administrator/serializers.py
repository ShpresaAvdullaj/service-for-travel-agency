from rest_framework import serializers
from .models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ["date_of_departure", "date_of_return"]

    def validate_rating(self):
        trip = Trip()
        if not (trip.date_return < trip.date_departure.date()):
            raise serializers.ValidationError(
                "Client should have some holiday. Please enter the correct date!!"
            )
        return self.date_of_return.date()
