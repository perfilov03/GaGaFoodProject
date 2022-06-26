from django.db import models
from restaurant.models import Restaurants
from dish.models import Dish

class Menu(models.Model):
    restaurant = models.ManyToManyField(verbose_name='Ресторан', to=Restaurants, related_name='menu')
    dish = models.ManyToManyField(verbose_name='Блюдо', to=Dish, related_name='menu')

    def __str__(self):
        return self.restaurant

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'