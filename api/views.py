from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.decorators import api_view
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
                test_id=pk
            )
        ]
        all_subtest_id = [
            i.id for i in Subtest.objects.filter(
                test_id=pk
            )
        ]
        all_questions = [
            i.name for i in Questions.objects.filter(
                subtest_id__in=all_subtest_id
            )
        ]
        all_questions_id = [
            i.id for i in Questions.objects.filter(
                subtest_id__in=all_subtest_id
            )
        ]
        all_answers = [
            i.name for i in Answers.objects.filter(
                question_id__in=all_questions_id
            )
        ]
        all_answers_id = [
            i.id for i in Answers.objects.filter(
                question_id__in=all_questions_id
            )
        ]
        all_scales = set(
            i.name for i in Scales.objects.filter(
                answers_id__in=all_answers_id
            )
        )
        all_scales_id = set(
            i.id for i in Scales.objects.filter(
                answers_id__in=all_answers_id
            )
        )
        all_interpret = [
            i.name for i in Interpretations.objects.filter(
                scale_id__in=list(all_scales_id)
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
    # Изменять тесты может ТОЛЬКО администратор
    permission_classes = (IsAdminUser, )


class UserAPIList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Список пользователей может просматривать ТОЛЬКО администратор
    permission_classes = (IsAdminUser, )


class UserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser)
# TODO:проверка на юзера (пользователь может менять
#      только свои личные данные). Для начала оставим
#      доступ только для администратора


class UserAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser)


@api_view(['POST'])
def UserCreate(request):
    serializers = UserSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

def test_list(request):
    tests = Test.objects.all()
    context = {'tests': tests}
    return render(request, 'tests.html', context)

def first_test(request):
    return render(request, 'firsttest.html')

def listests(request):
    return render(request, 'listests.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def profile(request):
    return render(request, 'profile.html') 