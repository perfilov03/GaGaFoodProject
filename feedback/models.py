from tabnanny import verbose
from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ваше имя")
    telephone = models.CharField(max_length=255, verbose_name="Номер телефона")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['id']
