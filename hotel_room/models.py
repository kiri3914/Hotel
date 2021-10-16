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
                                           on_delete=models.SET_NULL, related_name='category_furniture', null=True)
    slug = models.SlugField(max_length=255, verbose_name='Слаг')

    def __str__(self):
        return self.title


class Room(models.Model):
    number = models.CharField(max_length=255, verbose_name="Номер комнаты")
    category = models.ForeignKey(CategoryRoom, verbose_name='Категория комнаты', on_delete=models.SET_NULL, null=True)
    img = models.ImageField(verbose_name='Фото комнаты', upload_to='room', blank=True)
    furniture = models.ManyToManyField('Furniture', verbose_name='Мебель')
    count_windows = models.IntegerField(verbose_name='Количество Окан')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=255, verbose_name='Слаг')

    def __str__(self):
        return self.number
