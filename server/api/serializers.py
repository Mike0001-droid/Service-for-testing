from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import CustomUser
from .models import *
from rest_framework.renderers import JSONRenderer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["test"] = TestNameSerializer(
            instance.category, many=True).data
        return rep


class TestSerializer(serializers.ModelSerializer):
    # category_name = serializers.CharField(source='category.name')
    class Meta:
        model = Test
        fields = ('id', 'name', 'sdescription', 'subtest')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["subtest"] = SubTestNameSerializer(
            instance.test, many=True).data
        return rep


class SubTestSerializer(ModelSerializer):
    class Meta:
        model = Subtest
        fields = ('id', 'name', 'question')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["question"] = QuestionSerializer(
            instance.questions, many=True).data
        return rep


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'question_img', 'type_question', 'obligatory')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["answer"] = AnswerSerializer(
            instance.answers, many=True).data
        return rep
    
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'name', 'answer_img')

class TestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'name',)


class SubTestNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtest
        fields = ('id',)


class QuestionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name')

