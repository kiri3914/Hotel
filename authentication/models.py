from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
# dispatch - служит для проверки фотки
from django.dispatch import receiver


# AbstractUser - служит для регистрации и авторизации юзера
class User(AbstractUser):
    full_name = models.CharField(verbose_name='Полное имя', max_length=255, blank=True)
    age = models.PositiveIntegerField(default=18)
    image = models.ImageField(upload_to='user/profile')

    def __str__(self):
        return self.username