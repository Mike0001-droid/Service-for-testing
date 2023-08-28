from rest_framework import serializers
from users.models import CustomUser
from .models import *
from rest_framework.renderers import JSONRenderer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__" 

class TestSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Test
        fields = "__all__"

""" class AnswerSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Test
        fields = "__all__" """

class SubTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtest
        fields = "__all__"

class SubTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtest
        fields = "__all__"

