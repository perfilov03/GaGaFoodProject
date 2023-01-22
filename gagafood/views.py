from multiprocessing import AuthenticationError, context
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from gagafood.forms import AddFeedback
from .forms import *
from feedback.models import *
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from discount_coupons.models import Coupons
from authentication.models import User
from restaurant.models import *
from dish.models import Dish
from authentication.serializers import UserSerializer
from discount_coupons.serializers import CouponsSerializer
from restaurant.serializers import CategorySerializer, RestaurantsSerializer
from dish.serializers import DishSerializer
from rest_framework.generics import ListAPIView 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter
import django_filters.rest_framework
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


class DishPagination(PageNumberPagination):
    page_size = 10
    page_sizer_query_param = 'paginate_by'
    max_page_size = 20


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['email','first_name','last_name', 'telephone','address']
    ordering_fields = ['first_name', 'email', 'telephone']
    filterset_fields = ['first_name', 'email','telephone']


class CouponsViewSet(ModelViewSet):
    queryset = Coupons.objects.all()
    serializer_class =CouponsSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['title', 'description', 'percent']
    ordering_fields = ['percent', 'code']
    filterset_fields = ['title', 'percent']

    @action(methods=['Post'], detail=True, url_path='postCoupon') 
    def postCoupon(self, request, pk=None):
        serializer=self.serializer_class(data=request.data)
        serializer.save()
        return Response('Купон был создан')

    @action(methods=['GET'], detail=False)
    def get_data(self, request, **kwargs):
        coupons = Coupons.objects.all()
        return Response({'coupons': [coupon.title for coupon in coupons]})


class DishViewSet(ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class =DishSerializer
    pagination_class = DishPagination
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['title','price','weight']
    ordering_fields = ['price', 'weight']
    filterset_fields = ['title', 'restaurant']


class RestaurantsViewSet(ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class =RestaurantsSerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['title', 'category']
    ordering_fields = ['title', 'description', 'category']
    filterset_fields = ['title', 'category']


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =CategorySerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name','logo']
    ordering_fields = ['name']
    filterset_fields = ['name']


class GetDishView(ListAPIView):
    queryset = Dish.objects.filter(Q(price__lte=400)&Q(weight__lte=400))
    serializer_class = DishSerializer
    pagination_class = DishPagination
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['title', 'description', 'price','restaurant','price','weight']
    ordering_fields = ['price', 'weight']
    filterset_fields = ['title', 'restaurant']
    

class GetCategoryView(ListAPIView):
    queryset = Category.objects.order_by('-name')
    serializer_class = CategorySerializer
    filter_backends = [OrderingFilter, SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name','logo']
    ordering_fields = ['name']
    filterset_fields = ['name']


# @api_view(['GET'])
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
    category = Category.objects.all()[:8]
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


def edit_user(request, id):
    user = User.objects.get(id=id)
    return render(request, 'gagafood/edit.html', {'user': user})
