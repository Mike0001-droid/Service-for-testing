from rest_framework import serializers
from users.models import CustomUser
from .models import *
from rest_framework.renderers import JSONRenderer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__" 

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"