from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.permissions import *
from users.models import CustomUser
from .serializers import *
from .models import *
from .permissions import *


class TestAPIListForUsers(generics.ListCreateAPIView):
    queryset = Test.objects.filter(status="Опубликовано")
    serializer_class = TestSerializer
    permission_classes = (ViewTestNonDraft, )


class SubtestAPIListForUsers(generics.ListCreateAPIView):
    queryset = Subtest.objects.filter(test=1)
    serializer_class = SubTestSerializer
    permission_classes = (ViewTestNonDraft, )


def test_list(request):
    tests = Test.objects.all()
    context = {'tests': tests}
    return render(request, 'tests.html', context)


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
    if request.method == 'GET':
        return render(
            request,
            'test_passing.html',
            {'test': test}
        )
