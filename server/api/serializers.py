from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import MyUser
from .models import *
from rest_framework.renderers import JSONRenderer

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'question_img', 'type_question', 'obligatory', 'answer')

class SubtestSerializer(ModelSerializer):
    class Meta:
        model = Subtest
        fields = ('id', 'name', 'time_for_solution', 'description', 'question') 
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["question"] = QuestionSerializer(
            instance.questions, many=True).data
        return rep
    
class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id',)

class AnswerForQuestionSerializer(ModelSerializer):
    class Meta:
        model = AnswerForQuestion
        fields = '__all__'

class FullAnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class AttemptionSerializer(ModelSerializer):
    class Meta:
        model = Attemption
        fields = '__all__'


class FullAnswerForQuestionSerializer(ModelSerializer):
    class Meta:
        model = AnswerForQuestion
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["answer"] = FullAnswerSerializer(
            instance.answer).data
        return rep