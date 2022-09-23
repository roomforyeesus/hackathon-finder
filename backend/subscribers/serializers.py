from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Subscriber, Contest


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields =['name', 'email']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['email', 'name']
        
class SubscriberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email', 'name']
        
class ContestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contest
        fields = ['email', 'name', 'url', 'start_time', 'end_time', 'duration', 'description', 'in_24_hours']