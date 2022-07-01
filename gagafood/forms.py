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
    password1 = forms.CharField(label="Придумайте пароль:", widget=forms.TextInput(
        attrs={'class': 'registration__input', 'type': 'password'}))
    password2 = forms.CharField(label="Подтвердите пароль:", widget=forms.TextInput(
        attrs={'class': 'registration__input', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('first_name', 'telephone',
                  'email')
        #  'password1', 'password2'
        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'registration__input', 'placeholder': 'Анастасия'}),
            'last_name': forms.TextInput(
                attrs={'class': 'registration__input', 'placeholder': 'Анастасия'}),
            'telephone': forms.TextInput(
                attrs={'class': 'registration__input', 'placeholder': 'Анастасия'}),
        }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Введите ваш Email", widget=forms.TextInput(
        attrs={'class': 'login__input', 'placeholder': 'Анастасия'}))
    password = forms.CharField(label="Введите пароль:", widget=forms.TextInput(
        attrs={'class': 'Login__input', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('email', 'password')
