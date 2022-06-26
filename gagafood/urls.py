from django.urls import path
from .views import *
from restaurant.models import *

urlpatterns = [
    path('', index, name="home"),
    path('catalogue/', catalogue, name="catalogue"),
    path('restaurant/<int:restaurant_id>/',
         show_restaurant, name="restaurant"),
]
