from tabnanny import verbose
from django.db import models

class Restaurants (models.Model):
    title = models.CharField(verbose_name='Название ресторана', max_length=255)
    description = models.TextField(verbose_name='О ресторане')
    # menu = models.CharField(verbose_name='', max_length=255)
    logo = models.ImageField(verbose_name='Логотип', upload_to='restaurant')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'
