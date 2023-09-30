from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import CustomUser
from .models import *
from rest_framework.renderers import JSONRenderer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Test
        fields = "__all__"


class TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class SubtestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtest
        fields = '__all__'


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["test"] = TestNameSerializer(
            instance.category, many=True).data
        return rep


""" class CampaignSerializers(ModelSerializer):
    ads_type = serializers.CharField(source='ads_type.type')

    class Meta:
        model = Campaign
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["status"] = StatusSerializers(
            instance.status).data
        rep["regions"] = LocatSerializer(
            instance.regions.all(), many=True).data
        return rep """


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
