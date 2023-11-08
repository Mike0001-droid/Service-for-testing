from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from users.models import CustomUser
from django.core.handlers.wsgi import WSGIRequest
from rest_framework import status
from .func import *
from rest_framework.permissions import *
from .serializers import *
from .models import *
from .permissions import *

class CategoryViewSet(ViewSet):
    def list(self, request):
        queryset = Category.objects.filter(status='Опубликовано')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.filter(status='Опубликовано')
        user = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(user)
        return Response(serializer.data)

class TestViewSet(ViewSet):
    def list(self, request):
        queryset = Test.objects.filter(status='Опубликовано')
        serializer = TestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Test.objects.filter(status='Опубликовано')
        user = get_object_or_404(queryset, pk=pk)
        serializer = TestSerializer(user)
        return Response(serializer.data)
    
class SubTestViewSet(ViewSet):
    def list(self, request):
        queryset = Subtest.objects.filter(status='Опубликовано')
        serializer = SubTestSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Subtest.objects.filter(status='Опубликовано')
        user = get_object_or_404(queryset, pk=pk)
        serializer = SubTestSerializer(user)
        return Response(serializer.data)
    
    @action(
        detail=False,
        methods=['get'],
        url_path='by_test/(?P<id>[a-zA-Z0-9_]+)',
        url_name='by-test',
    )
    def subtest_by_test(self, request, id):
        queryset = Subtest.objects.filter(test_id=id)
        serializer = SubTestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class QuestionViewSet(ViewSet):
    def list(self, request):
        queryset = Question.objects.filter(status='Опубликовано')
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.filter(status='Опубликовано')
        user = get_object_or_404(queryset, pk=pk)
        serializer = QuestionSerializer(user)
        return Response(serializer.data)
    
    @action(
        detail=False,
        methods=['get'],
        url_path='by_subtest/(?P<id>[a-zA-Z0-9_]+)',
        url_name='by-subtest',
    )
    def subtest_by_test(self, request, id):
        queryset = Question.objects.filter(subtest_id=id)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



def test_list(request):
    return render(request, 'tests.html')


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')


def pass_the_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    """ attemption = Attemption.objects.filter(
        test_id=test.pk, user_id=request.user) """
    if request.method == 'GET':
        return render(
            request,
            'test_passing.html',
            {'test': test}
        )
    else:
        percentage = get_test_result(request, test,)

        return render(
            request, 'test_result.html',
            {'percentage': percentage,

             }
        )
