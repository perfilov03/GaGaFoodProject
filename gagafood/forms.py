from cProfile import label
from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authentication.models import User


class AddFeedback(forms.Form):
    name = forms.CharField(max_length=255, label="Ваше имя", widget=forms.TextInput(
        attrs={'class': 'feedback__input', 'placeholder': 'Анастасия'}))
    telephone = forms.CharField(max_length=255, label="Номер телефона", widget=forms.TextInput(
        attrs={'class': 'feedback__input', 'placeholder': '+7 (999) 999 99-99'}))


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label="Придумайте пароль", widget=forms.TextInput(
        attrs={'class': 'registration__input', 'type': 'password'}))
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.TextInput(
        attrs={'class': 'registration__input', 'type': 'password'}))
    first_name = forms.CharField(label="Ваше имя", widget=forms.TextInput(
        attrs={'class': 'registration__input',
               'placeholder': 'Анастасия'}))
    email = forms.CharField(label="Электронная почта", widget=forms.TextInput(
        attrs={'class': 'registration__input', 'placeholder': 'lady@gaga.com'}))
    telephone = forms.CharField(label="Номер телефона", widget=forms.TextInput(
        attrs={'class': 'registration__input', 'placeholder': '+7 (999) 999 99-99'}))

    class Meta:
        model = User
        fields = ('first_name', 'telephone',
                  'email')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'registration__input',
                       'placeholder': 'Анастасия'}),
            'email': forms.TextInput(
                attrs={'class': 'registration__input', 'placeholder': 'lady@gaga.com'}),
            'telephone': forms.TextInput(
                attrs={'class': 'registration__input', 'placeholder': '+7 (999) 999 99-99'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="E-Mail", widget=forms.TextInput(
        attrs={'class': 'authorization__input', 'placeholder': 'lady@gaga.com'}))
    password = forms.CharField(label="Пароль", widget=forms.TextInput(
        attrs={'class': 'authorization__input', 'type': 'password'}))
