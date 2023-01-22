from rest_framework import serializers
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'first_name', 'email', 'last_name', 'telephone', 'address', 'is_active', 'is_staff', 'is_superuser']
