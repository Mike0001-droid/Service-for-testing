from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from .func import *
from rest_framework.permissions import *
from .serializers import *
from .models import *
from .permissions import *
from drf.settings import SECRET_KEY
from .schemas import AttemptSchema
import itertools
import jwt

class SubtestViewSet(ViewSet):
    def list(self, request):
        queryset = Subtest.objects.all()
        serializer = SubtestSerializer(queryset, many=True)
        return Response(serializer.data)
    
class AttemptViewSet(ViewSet):
    @action(detail=False, methods=['post'], schema=AttemptSchema())
    def create_attempt(self, request):
        test_id=request.data['test']
        patternAnswer_id=request.data['patternAnswer'],
        question_id=request.data['question'],
        answers = {}
        answers['answers'] = (list(Answer.objects.filter(
            patternAnswer_id = patternAnswer_id,
            question_id = question_id,
            test_id = test_id
        ).values_list('id', flat=True)))
        data = {
            "answer": answers,
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
            data['answer']['answers'] = instance.answer['answers'] + \
                                        data['answer']['answers']
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
        for i in queryset.answer['answers']:
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
                        "Сумма баллов": k['scores'],
                        "Текст": j['description'],
                        "Шкала": k['scale_id']
                    })  
        return Response(response)
