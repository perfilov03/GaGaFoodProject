from django.db import models
from restaurant.models import Restaurants


class Dish(models.Model):
    title = models.CharField(verbose_name='Название блюда', max_length=255)
    restaurant = models.ForeignKey(
        Restaurants, verbose_name='Ресторан', related_name='dish', on_delete=models.PROTECT, null=True)
    description = models.TextField(verbose_name='Описание')
    cover = models.ImageField(verbose_name='Фотография', upload_to='dish')
    weight = models.IntegerField(verbose_name='Вес/количество (граммы)')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['restaurant', 'title']
