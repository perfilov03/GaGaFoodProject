from django.urls import path
from .views import *
from restaurant.models import *

urlpatterns = [
    path('', index, name="home"),
    path('catalogue/', catalogue, name="catalogue"),
    path('restaurant/<int:restaurant_id>/',
         show_restaurant, name="restaurant"),
    path('registration/', RegisterUser.as_view(), name="registration"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', logout_user, name="logout"),
    path('profile/', profile, name='profile'),
    path('basket/', basket, name='basket'),
]
