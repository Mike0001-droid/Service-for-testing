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


class AnswerViewSet(ViewSet):
    @action(detail=False, methods=['post'], schema=AttemptSchema())
    def return_answer(self, request):
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
        

class SummScoreViewSet(ViewSet):
    def retrieve(self, request, pk):
        queryset = Attemption.objects.get(id=pk)
        all_scales = []
        all_scales_id = set()
        for i in queryset.answer['answers']:
            answer_obj = Answer.objects.get(id=i)
            all_scales_id.add(answer_obj.scale.id)
            all_scales.append({
                'scale_id': answer_obj.scale.id,
                'answer': i
            })
        scales_answer = []
        for k in all_scales:
            summ_score = sum(list(Answer.objects.filter(id=k['answer'], scale_id=k['scale_id']).values_list('score', flat=True)))
            scales_answer.append({'scale_id': k['scale_id'], 'scores': summ_score})
        key = lambda x: x['scale_id']
        scores_summ = [
            {'scale_id': k, 'scores': sum(int(x['scores']) for x in g)} 
            for k, g in itertools.groupby(sorted(scales_answer, key=key), key=key)
        ]
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
