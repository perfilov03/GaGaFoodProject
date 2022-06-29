from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from gagafood.forms import AddFeedback
from restaurant.models import *
from dish.models import Dish
from .forms import *
from feedback.models import *


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
    return render(request, 'gagafood/index.html', {'form': form})


def catalogue(request):
    restaurants = Restaurants.objects.all()
    category = Category.objects.all()
    context = {
        'restaurants': restaurants,
        'category': category,
        # 'cat_selected': restaurant_id,
    }
    return render(request, 'gagafood/catalogue.html', context=context)


def show_restaurant(request, restaurant_id):
    restaurants = Restaurants.objects.all()
    context = {
        'restaurants': restaurants,
        'restaurant_selected': restaurant_id,
        'dish': Dish.objects.all(),
        # 'dish': dish,
    }
    return render(request, 'gagafood/restaurant.html', context)


def show_menu(request, restaurant_id):
    dish = Dish.objects.all()


# class RegisterUser(DataMixin, CreateView):
#     form_class = UserCreationform
#     template_name = 'gagafood/registration.html'
#     success_url = reverse_lazy('login')

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="Регистрация")
#         return dict(list(context.items()) + list(c_def.item()))

def profile(request):
    return render(request, 'gagafood/profile.html')


# def authorization(request):
#     return render(request, 'gagafood/login.html')
