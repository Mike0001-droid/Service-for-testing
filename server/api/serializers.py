from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class FilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(status='опубликовано')
        return super(FilteredListSerializer, self).to_representation(data)
    
class TestNameSerializer(ModelSerializer):
    class Meta:
        list_serializer_class = FilteredListSerializer
        model = Test
        fields = ('id', 'name')

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["test"] = TestNameSerializer(
            instance.author, many=True).data
        return rep
    
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["test"] = TestNameSerializer(
            instance.category, many=True).data
        return rep
    
class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name',)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["test"] = TestNameSerializer(
            instance.topic, many=True).data
        return rep

class SubTestNameSerializer(ModelSerializer):
    class Meta:
        model = Subtest
        list_serializer_class = FilteredListSerializer
        fields = ('id', 'name')

class TestSerializer(ModelSerializer):
    author_name = serializers.CharField(source='author.name')
    class Meta:
        model = Test
        fields = ('id', 'name', 'author_name', 'description_1')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["subtest"] = SubTestNameSerializer(
            instance.test, many=True).data
        return rep
    
class PatternAnswerSerializer(ModelSerializer):
    class Meta:
        model = PatternAnswer
        fields = ('id', 'name', 'answer_img')

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'name', 'question_img', 'type_question', 'obligatory', 'answer')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["answer"] = PatternAnswerSerializer(
            instance.answer, many=True).data
        return rep

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
    answers = serializers.CharField(source='answer')
    class Meta:
        model = Attemption
        fields = ('test', 'user', 'answers')


class FullAnswerForQuestionSerializer(ModelSerializer):
    class Meta:
        model = AnswerForQuestion
        fields = '__all__'
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["answer"] = FullAnswerSerializer(
            instance.answer).data
        return rep