from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from administrator.models import Trip
from .serializers import TripModelSerializer


class TripListCreateView(generics.ListCreateAPIView):
    queryset = Trip.objects.order_by('-pk').all()
    serializer_class = TripModelSerializer
    pagination_class = PageNumberPagination


class TripDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripModelSerializer
