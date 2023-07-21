from rest_framework import serializers
from .models import *
from rest_framework.renderers import JSONRenderer


""" class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__" """

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"