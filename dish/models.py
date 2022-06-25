from django.db import models
from restaurant.models import Restaurants

class Dish(models.Model):
    title = models.CharField(verbose_name='Название блюда', max_length=255)
    restaurant = models.ManyToManyField(verbose_name='Ресторан', to=Restaurants, related_name='dish')
    description = models.TextField(verbose_name='Описание')
    cover = models.ImageField(verbose_name='Фотография', upload_to='dish')
    weight = models.IntegerField(verbose_name='Вес/количество (граммы)')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'