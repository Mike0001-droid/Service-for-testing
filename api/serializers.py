from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('login', 'first_name', 'last_name')


class SubtestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtest
        fields = ('name', 'test_id')
