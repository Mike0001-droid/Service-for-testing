from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import MyUser
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


class AttemptSerializer(ModelSerializer):
    class Meta:
        model = Attemption
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["answers"] = AnswerSerializer(
            instance.answers.all(), many=True
        ).data
        return rep


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


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'name', 'answer_img')


class AnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class ScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scale
        fields = '__all__'


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class InterpretationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interpretation
        fields = '__all__'
