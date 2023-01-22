from django.urls import include,path
from django.conf.urls import include
from .views import *
from restaurant.models import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('user', UserViewSet)
router.register('coupons',CouponsViewSet)
router.register('dish',DishViewSet)
router.register('restaurants',RestaurantsViewSet)
router.register('category',CategoryViewSet)


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
    path('edit/', edit_user, name='edit'),
    path('api/', include(router.urls)),
    path('api/dish-filter/', GetDishView.as_view()),
    path('api/category-filter/', GetCategoryView.as_view()),
]
