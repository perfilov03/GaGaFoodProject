from django.db import models
from restaurant.models import Restaurants
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_weight(value):
    if value < -1:
        raise ValidationError(
            _('%(value)s Вес не может быть отрицательным'),
            params={'value': value})

def validate_price(value):
    if value < -1:
        raise ValidationError(
            _('%(value)s Цена не может быть отрицательной'),
            params={'value': value})


class Dish(models.Model):
    title = models.CharField(verbose_name='Название блюда', max_length=255)
    restaurant = models.ForeignKey(
        Restaurants, verbose_name='Ресторан', related_name='dish', on_delete=models.PROTECT, null=True)
    description = models.TextField(verbose_name='Описание')
    cover = models.ImageField(verbose_name='Фотография', upload_to='dish')
    weight = models.IntegerField(verbose_name='Вес/количество (граммы)', validators=[validate_weight])
    price = models.IntegerField(verbose_name='Цена', validators=[validate_price])
    
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['restaurant', 'title']
