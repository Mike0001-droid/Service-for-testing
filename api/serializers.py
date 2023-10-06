from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import CustomUser
from .models import *
from rest_framework.renderers import JSONRenderer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["test"] = TestNameSerializer(
            instance.category, many=True).data
        return rep


class TestSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Test
        fields = ('id', 'name', 'subtest')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["subtest"] = SubTestSerializer(
            instance.test, many=True).data
        return rep


class SubTestSerializer(ModelSerializer):
    # test = serializers.CharField(source='test.name')
    class Meta:
        model = Subtest
        fields = ('id', 'name', 'question')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["question"] = QuestionNameSerializer(
            instance.questions, many=True).data
        return rep


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'answer')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["answer"] = AnswerNameSerializer(
            instance.answers, many=True).data
        return rep


class TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name', 'description_1')


class QuestionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name')


class AnswerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'name')
