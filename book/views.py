from django.shortcuts import render
from .models import Booking
from .serializers import BookSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class BookingListCreateAPIView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializers


class BookingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookSerializers
