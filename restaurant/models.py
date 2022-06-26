from tabnanny import verbose
from django.db import models
from django.urls import reverse


class Restaurants (models.Model):
    title = models.CharField(verbose_name='Название ресторана', max_length=255)
    category = models.ForeignKey(
        'Category', verbose_name='Категория ресторана', on_delete=models.PROTECT, null=True)
    description = models.TextField(verbose_name='О ресторане')
    # menu = models.CharField(verbose_name='', max_length=255)
    logo = models.ImageField(verbose_name='Логотип', upload_to='restaurant')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('restaurant', kwargs={'restaurant_id': self.pk})

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'


class Category (models.Model):
    name = models.CharField(
        verbose_name='Название категории', max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории ресторанов'
