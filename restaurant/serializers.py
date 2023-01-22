from rest_framework import serializers
from .models import Restaurants, Category

class RestaurantsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Restaurants
        fields = ['url', 'title', 'category', 'description', 'logo']


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ['url', 'name', 'logo']

    


