from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SubtestAPIView(generics.ListAPIView):
    queryset = Subtest.objects.all()
    serializer_class = SubtestSerializer
