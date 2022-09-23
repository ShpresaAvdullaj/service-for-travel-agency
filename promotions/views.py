from django.shortcuts import render
from administrator.models import Trip


def promoted_trips(request):
    trips = Trip.objects.filter(promoted=True)
    context = {
        "trips": trips,
    }
    return render(request, "promotions/promoted.html", context)
