from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Feedback
        fields = ['url', 'name', 'telephone']

    


