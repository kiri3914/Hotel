from django.db import models
from hotel_room.models import Room
from authentication.models import User


class Booking(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name="Номер", on_delete=models.SET_NULL, null=True)
    date_from = models.DateTimeField(auto_now_add=False, verbose_name="С какого числа")
    date_bevor = models.DateTimeField(auto_now_add=False, verbose_name="до какого числа")
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.user

