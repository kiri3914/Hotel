from rest_framework import serializers
from book.models import *


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = 'id', 'user', 'room', 'date_from', 'date_bevor', 'is_publish'
