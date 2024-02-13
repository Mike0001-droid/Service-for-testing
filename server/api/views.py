from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework import status
from .func import *
from rest_framework.permissions import *
from .serializers import *
from .models import *
from .permissions import *
from drf.settings import SECRET_KEY
from .schemas import AttemptSchema
import jwt



class PatternAnswerViewSet(ViewSet):
    schema = AttemptSchema()
    def list(self, request): 
        queryset = PatternAnswer.objects.filter(status='опубликовано')
        serializer = PatternAnswerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['post'], schema=AttemptSchema())
    def return_list(self, requset):
        queryset = PatternAnswer.objects.filter(status='опубликовано')
        serializer = PatternAnswerSerializer(queryset, many=True)
        return Response(serializer.data)
    
class AnswerViewSet(ViewSet):
    @action(detail=False, methods=['post'], schema=AttemptSchema())
    def return_answer(self, request):
        queryset = Answer.objects.filter(
            patternAnswer_id=request.data['patternAnswer'],
            question_id = request.data['question'],
            test_id = request.data['test']
        )
        serializer = AnswerSerializer(queryset, many=True)
        for x in serializer.data:
            x['answer'] = x.pop('id')
            x.update(user=1)
        serializer1 = AnswerForQuestionSerializer(data=serializer.data, many=True)
        if serializer1.is_valid():
            serializer1.save()
        return Response(serializer1.data)

class SummScoreViewSet(ViewSet):
    def list(self, request): 
        queryset = AnswerForQuestion.objects.all()
        serializer = FullAnswerForQuestionSerializer(queryset, many=True)
        return Response(serializer.data)





