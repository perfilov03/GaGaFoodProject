from multiprocessing import AuthenticationError, context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from gagafood.forms import AddFeedback
from restaurant.models import *
from dish.models import Dish
from .forms import *
from feedback.models import *
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from discount_coupons.models import Coupons


def index(request):
    if request.method == 'POST':
        form = AddFeedback(request.POST)
        if form.is_valid():
            try:
                Feedback.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Ошибка отправки данных')
    else:
        form = AddFeedback()
    # category = Category.objects.filter(name='Фастфуд')
    category = Category.objects.all()
    restaurants = Restaurants.objects.filter(category=1)

    return render(request, 'gagafood/index.html', {'form': form, 'category': category, 'title': 'GaGaFood'})


def catalogue(request):
    restaurants = Restaurants.objects.all()
    category = Category.objects.all()
    context = {
        'restaurants': restaurants,
        'category': category,
        'title': 'Каталог ресторанов',
        # 'cat_selected': restaurant_id,
    }
    return render(request, 'gagafood/catalogue.html', context=context)


def show_restaurant(request, restaurant_id):
    restaurants = Restaurants.objects.all()
    context = {
        'restaurants': restaurants,
        'restaurant_selected': restaurant_id,
        'dish': Dish.objects.all(),
        'title': 'Ресторан',
    }
    return render(request, 'gagafood/restaurant.html', context)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'gagafood/registration.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def profile(request):
    return render(request, 'gagafood/profile.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'gagafood/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('profile')


def profile(request):
    coupons = Coupons.objects.all()
    context = {
        'title': 'Профиль',
        'coupons': coupons,
    }

    return render(request, 'gagafood/profile.html', context=context)


def logout_user(request):
    logout(request)
    return redirect('login')


def basket(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, 'gagafood/basket.html', context=context)
