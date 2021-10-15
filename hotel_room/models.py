from django.db import models


class CategoryRoom(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория комнаты')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')

    def __str__(self):
        return self.title


class CategoryFurniture(models.Model):
    title = models.CharField(max_length=255, verbose_name='Категория Мебели')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')

    def __str__(self):
        return self.title


class Furniture(models.Model):
    title = models.CharField(max_length=255, verbose_name='Мебель')
    category_furniture = models.ForeignKey(CategoryFurniture, verbose_name='Категория Мебели',
                                           on_delete=models.SET_NULL, related_name='category_furniture')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')

    def __str__(self):
        return self.title


class Room(models.Model):
    number = models.CharField(max_length=255, verbose_name="Номер комнаты")
    category = models.ForeignKey(CategoryRoom, verbose_name='Категория комнаты', on_delete=models.SET_NULL)
    img = models.ImageField(verbose_name='Фото комнаты', upload_to='/image/room', blank=True)
    # image = models.ImageField(verbose_name='Фото комнаты', upload_to='/image/room', blank=True)
    # jpg = models.ImageField(verbose_name='Фото комнаты', upload_to='/image/room', blank=True)
    furniture = models.ForeignKey(Furniture, verbose_name='Мебель', on_delete=models.SET_NULL)
    count_windows = models.IntegerField(verbose_name='Количество Окан')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')

    def __str__(self):
        return self.number
