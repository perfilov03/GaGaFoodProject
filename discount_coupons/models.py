from django.db import models
from django.contrib.auth.models import Group


class Coupons (models.Model):
    title = models.CharField(verbose_name='Название акции', max_length=255)
    description = models.TextField(verbose_name='Об акции')
    percent = models.CharField(verbose_name='Процент скидки', max_length=3)
    code = models.CharField(verbose_name='Код', max_length=255, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'
        ordering = ['percent', 'code', ]
