from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from .serializers import *
from .models import *
from .permissions import *

    
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    @action(methods=['get'], detail=True)
    def test(self, request, pk=None):
        tests = Test.objects.get(id=pk)
        all_subtest = [
            i.name for i in Subtest.objects.filter(
                test_id = pk
            )
        ]
        all_subtest_id = [
            i.id for i in Subtest.objects.filter(
                test_id = pk
            )
        ]
        all_questions = [
            i.name for i in Questions.objects.filter(
                subtest_id__in = all_subtest_id
            )
        ]
        all_questions_id = [
            i.id for i in Questions.objects.filter(
                subtest_id__in = all_subtest_id
            )
        ]
        all_answers = [
            i.name for i in Answers.objects.filter(
                question_id__in = all_questions_id
            )
        ]
        all_answers_id = [
            i.id for i in Answers.objects.filter(
                question_id__in = all_questions_id
            )
        ]
        all_scales = set(
            i.name for i in Scales.objects.filter(
                answers_id__in = all_answers_id
            )
        )
        all_scales_id = set(
            i.id for i in Scales.objects.filter(
                answers_id__in = all_answers_id
            )
        )
        all_interpret = [
            i.name for i in Interpretations.objects.filter(
                scale_id__in = list(all_scales_id)
            )
        ]  
        return Response({
            'tests': tests.name,
            'subtest': all_subtest,
            'questions': all_questions,
            'answers': all_answers,
            'scales': all_scales,
            'interpretation': all_interpret 
        }) 

class TestAPIListForUsers(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (ViewTestNonDraft, )

class TestAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAdminUser)# Изменять тесты может ТОЛЬКО администратор

class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser)# Список пользователей может просматривать ТОЛЬКО администратор

class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser)
#TODO: проверка на юзера (пользователь может менять 
#      только свои личные данные). Для начала оставим
#      доступ только для администратора

class UserAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser)
