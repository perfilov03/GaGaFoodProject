from django import forms
from .models import *


class AddFeedback(forms.Form):
    name = forms.CharField(max_length=255, label="Ваше имя")
    telephone = forms.CharField(max_length=255, label="Номер телефона")
