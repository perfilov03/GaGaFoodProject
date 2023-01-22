from rest_framework import serializers
from .models import Coupons

class CouponsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Coupons
        fields = ['url', 'title', 'description', 'percent', 'code']

     
