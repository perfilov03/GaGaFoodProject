from tabnanny import verbose
from django.db import models
from simple_history.models import HistoricalRecords

class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ваше имя")
    telephone = models.CharField(max_length=255, verbose_name="Номер телефона")
    
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['id']
