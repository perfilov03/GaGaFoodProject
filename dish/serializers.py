from rest_framework import serializers
from .models import Dish

class DishSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Dish
        fields = ['url', 'title', 'description', 'cover', 'weight', 'price', 'restaurant']




