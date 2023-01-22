from django.db import models
from django.contrib.auth.models import Group
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


# def validate_percent(value):
#     if value < -1:
#         raise ValidationError(
#             _('%(value)s Процент скидки не может быть отрицательным'),
#             params={'value': value})
#     elif value > 100:
#         raise ValidationError(
#             _('%(value)s Процент скидки не может быть больше 100'),
#             params={'value': value})

class Coupons (models.Model):
    title = models.CharField(verbose_name='Название акции', max_length=255)
    description = models.TextField(verbose_name='Об акции')
    percent = models.CharField(verbose_name='Процент скидки', max_length=3)
    code = models.CharField(verbose_name='Код', max_length=255, unique=True)
    
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'
        ordering = ['percent', 'code', ]
