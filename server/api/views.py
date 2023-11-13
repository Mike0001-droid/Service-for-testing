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
from .schemas import AttemptSchema, ScoreSchema
import operator
from itertools import chain

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
    def question_by_subtest(self, request, id):
        queryset = Question.objects.filter(subtest_id=id)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AttemptListViewSet(ViewSet):
    def list(self, request):
        queryset = Attemption.objects.all()
        serializer = AttemptSerializer(queryset, many=True)
        return Response(serializer.data)
    
class AttemptViewSet(ViewSet):
    
    schema = AttemptSchema()
    @action(detail=False, methods=['post'])
    def create_attempt(self, request):
        if request.data['attempt'] == 'null':
            serializer = AttemptSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif request.data['attempt'] != 'null':
            pk = request.data['attempt']
            attempt = get_object_or_404(Attemption, pk=request.data['attempt'])
            answers_id = Answer.objects.filter(id__in=request.data['answers'])
            thing = [i.pk for i in list(chain(attempt.answers.all(), answers_id))]
            request.data['answers'] = thing
            try:
                instance = Attemption.objects.get(pk=pk)
            except:
                
                return Response({"error": "Object does not exists"})
            serializer = AttemptSerializer(data=request.data, instance=instance)
            serializer.is_valid()
            serializer.save()
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScaleListViewSet(ViewSet):
    def list(self, request):
        answer_id = [i.answer.values_list("id", flat=True) for i in Scale.objects.all()]
        scores = [sum(list(Score.objects.filter(answer__in=list(i)).values_list("score", flat=True))) for i in answer_id]  
        scales_names = [i.pk for i in Scale.objects.all()]
        resp = dict(zip(scales_names, scores))
        #(round(x, 3) * 100) 
        objects = [list(Interpretation.objects.filter(scale=k).values_list("finish_score", flat=True)) for k in scales_names]

        """ for i in range(len(scores)):
            print(i)
            print(len(objects))
            result = [x/y[i] for x in scores for y in objects]
 """
        for i in range(len(scores)):
            print(objects[i])
        
            
        
        print(len(objects))
        queryset = Scale.objects.all()
        serializer = ScaleSerializer(queryset, many=True)
        return Response(resp)
    
class AnsListViewSet(ViewSet):
    def list(self, request):
        queryset = Answer.objects.all()
        serializer = AnsSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
class ScoreListViewSet(ViewSet):
    def list(self, request):
        queryset = Score.objects.all()
        serializer = ScoreSerializer(queryset, many=True)
        return Response(serializer.data)
    @action(
        detail=False,
        methods=['get'],
        url_path='by_answers_id/(?P<id>[a-zA-Z0-9_]+)',
        url_name='by-answers',
    )
    def scorebyanswer(self, request, id):
        attempt_id = get_object_or_404(Attemption, pk=id)
        queryset = Score.objects.filter(answer__in = attempt_id.answers.all())
        serializer = ScoreSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InterpretationListViewSet(ViewSet):
    def list(self, request):
        queryset = Interpretation.objects.all()
        serializer = InterpretationSerializer(queryset, many=True)
        return Response(serializer.data)

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
            {'percentage': percentage,}
        )
