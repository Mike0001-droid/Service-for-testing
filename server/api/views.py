from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .func import *
from rest_framework.permissions import *
from .serializers import *
from .models import *
from .permissions import *
from drf.settings import SECRET_KEY
from .schemas import AttemptSchema
import itertools

class SeoSchemeGenericViewSet(GenericViewSet):
    queryset = SeoScheme.objects.all()
    serializer_class = SeoSchemeSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(ViewSet):
    def list(self, request): 
        queryset = Category.objects.filter(status='опубликовано')
        serializer = CategorySerializer(queryset, many=True)
        response = [i for i in serializer.data if len(i['test'])!=0]
        return Response(response)

class AuthorViewSet(ViewSet):
    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        response = [i for i in serializer.data if len(i['test'])!=0]
        return Response(response)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(user)
        response = [i for i in serializer.data if len(i['test'])!=0]
        return Response(response)
    
class TopicViewSet(ViewSet):
    def list(self, request):
        queryset = Topic.objects.filter(status='опубликовано')
        serializer = TopicSerializer(queryset, many=True)
        response = [i for i in serializer.data if len(i['test'])!=0]
        return Response(response)

    def retrieve(self, request, pk=None):
        queryset = Topic.objects.filter(status='опубликовано')
        user = get_object_or_404(queryset, pk=pk)
        serializer = TopicSerializer(user)
        response = [i for i in serializer.data if len(i['test'])!=0]
        return Response(response)

class TestViewSet(GenericViewSet):
    queryset = Test.objects.filter(status='опубликовано')
    serializer_class = TestNameSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

    def list(self, request, *args, **kwargs):
        queryset = Test.objects.filter(status='опубликовано')
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__iregex=name)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Test.objects.filter(status='опубликовано')
        user = get_object_or_404(queryset, pk=pk)
        serializer = TestSerializer(user)
        sub_id = [i['id'] for i in serializer.data['subtest']]
        quest_id = list(filter(None, list(Subtest.objects.filter(
            id__in=sub_id).values_list('questions', flat=True))))  
        response = {'count': len(quest_id)}
        response.update(serializer.data)
        return Response(response)
    
    
class SubtestViewSet(ViewSet):
    def list(self, request):
        queryset = Subtest.objects.filter(status='опубликовано')
        serializer = SubtestSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Subtest.objects.filter(status='опубликовано')
        user = get_object_or_404(queryset, pk=pk)
        serializer = SubtestSerializer(user)
        return Response(serializer.data)
    
    @action(
            detail=False,
            methods=['get'],
            url_path='by_test/(?P<id>[a-zA-Z0-9_]+)',
            url_name='by-test',
        )
    def subtest_by_test(self, request, id):
        queryset = Subtest.objects.filter(test_id=id)
        serializer = SubtestSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AttemptViewSet(ViewSet):
    def list(self, request):
        queryset = Attemption.objects.all()
        serializer = AttemptionSerializer(queryset, many=True)
        for i in serializer.data:
            print(i['answers'])
        return Response(serializer.data)


    @action(detail=False, methods=['post'], schema=AttemptSchema())
    def create_attempt(self, request):
        test_id=request.data['test']
        question_id=request.data['question'],
        answers = (list(Answer.objects.filter(
            patternAnswer_id__in = list(request.data['answers']),
            question_id = question_id,
            test_id = test_id
        ).values_list('id', flat=True)))
        data = {
            "answers": answers,
            "test": test_id,
            "user": 1,    
        } 
        if 'attempt' not in request.data: 
            serializer = AttemptionSerializer(data=data)
            if serializer.is_valid():
                serializer.save()        
                return Response(serializer.data)   
        elif 'attempt' in request.data:
            pk = request.data['attempt']
            try:
                instance = Attemption.objects.get(pk=pk)
            except:
                return Response({"error": "Object does not exists"})
            data['answers'] = instance.answers + data['answers']
            serializer = AttemptionSerializer(data=data, instance=instance)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
        
    @action(
        detail=False,
        methods=['get'],
        url_path='by_attempt_id/(?P<pk>[a-zA-Z0-9_]+)',
        url_name='by-attempt',
    )
    def attemptbyid(self, request, pk):
        #Создаём массив со всеми шкалами теста
        queryset = Attemption.objects.get(id=pk)
        all_scales = []
        for i in queryset.answers:
            answer_obj = Answer.objects.get(id=i)
            all_scales.append({
                'scale_id': answer_obj.scale.id,
                'answer': i
            })

        #Создаем массив словарей с айдишником шкалы и баллов по шкале
        scales_answer = []
        for k in all_scales:
            summ_score = sum(list(Answer.objects.filter(id=k['answer'], scale_id=k['scale_id']).values_list('score', flat=True)))
            scales_answer.append({'scale_id': k['scale_id'], 'scores': summ_score})
        #Суммируем баллы относительно одинаковых шкал, данные храним так же в виде массива словарей
        key = lambda x: x['scale_id']
        scores_summ = [
            {'scale_id': k, 'scores': sum(x['scores'] for x in g)} 
            for k, g in itertools.groupby(sorted(scales_answer, key=key), key=key)
        ]
        
        #Достаем объекты интерпретаций, относительно шкал и делаем выборку относительно суммы баллов по данной шкале
        #Записи добавляем в массив "response" и отдаем пользователю в качестве результатов пройденного теста
        response = []
        for k in scores_summ:
            interp_obj = Interpretation.objects.filter(scale_id=k['scale_id']).values("start_score", "finish_score", "description")
            for j in interp_obj:
                if (j['start_score'] <= k['scores'] <= j['finish_score']) or \
                   (j['start_score'] <= k['scores'] >= j['finish_score']):
                    response.append({
                        "scores_summ": k['scores'],
                        "text_interpret": j['description'],
                        "scale": k['scale_id']
                    })  
        otvet = {"url": f"https://tests.flexidev.ru/attempt/{pk}", "data": response}
        print(response)
        return Response(otvet)
