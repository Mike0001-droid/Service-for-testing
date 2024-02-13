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
    def retrieve(self, request, pk): 
        queryset = AnswerForQuestion.objects.filter(answer_id__test = pk) 
        serializer = FullAnswerForQuestionSerializer(queryset, many=True)
        all_scales = set()
        for i in serializer.data:
            all_scales.add(i['answer']['scale'])
        scores_summ = []
        for k in all_scales:
            summ_score = sum(list(Answer.objects.filter(scale_id = k).values_list('score', flat=True)))
            scores_summ.append({'scale_id': k, 'scores': summ_score})

        response = []
        for k in scores_summ:
            interp_obj = Interpretation.objects.filter(scale_id = k['scale_id']).values("start_score", "finish_score", "description")
            
            for j in interp_obj:
                if (j['start_score'] <= k['scores'] <= j['finish_score']) or (j['start_score'] <= k['scores'] >= j['finish_score']):
                    response.append({
                        "Сумма баллов": k['scores'],
                        "Текст": j['description'],
                        "Шкала": k['scale_id']
                    })  
            
        return Response(response)





