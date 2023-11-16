from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework import status
from .func import *
from rest_framework.permissions import *
from .serializers import *
from .models import *
from .permissions import *
from .schemas import AttemptSchema
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
    
    @action(
        detail=False,
        methods=['get'],
        url_path='by_attempt_id/(?P<id>[a-zA-Z0-9_]+)',
        url_name='by-attempt',
    )
    def attemptbyid(self, request, id):
        attempt_id = get_object_or_404(Attemption, pk=id)
        scales_pk = set(attempt_id.answers.values_list("scale_answer", flat=True))
        scores = []
        for k in scales_pk:
            if len(Answer.objects.filter(scale_answer=k)) > 1:
                scores.append(sum(list(Score.objects.filter(answer__in=list(Answer.objects.filter(scale_answer=k).values_list("id", flat=True))).values_list("score", flat=True))))
            else:
                 
                scores.append(sum(list(Score.objects.filter(answer=get_object_or_404(Answer, scale_answer=k).pk).values_list("score", flat=True))))
        
        interp_text = [list(Interpretation.objects.filter(scale=k).values_list("text", flat=True)) for k in scales_pk]
        finish_scores = [list(Interpretation.objects.filter(scale=k).values_list("finish_score", flat=True)) for k in scales_pk]
        interpretations_name = [list(Interpretation.objects.filter(scale=k).values_list("name", flat=True)) for k in scales_pk]
        interpretations_json = []
        for i in range(len(interpretations_name)):
            if len(interpretations_name[i])>1:
                interpretations_json.append([{"interp_name": interpretations_name[i][k], "percent": 0, "description": interp_text[i][k]} for k in range(len(interpretations_name[i]))])
            else:
                interpretations_json.append([{"interp_name": interpretations_name[i][0], "percent": 0, "description": interp_text[i][0]}])
        percentage = []
        interp_rercentage = []
        for t in range(len(scales_pk)):
            finish_scores = [y for y in finish_scores]
            scores_1 = scores
            if len(finish_scores[t]) > 1:
                percentage.append([100.0 if (round(scores_1[t]/finish_scores[t][k], 3)*100)>100.0 else (round(scores_1[t]/finish_scores[t][k], 3)*100) for k in range(len(finish_scores[t]))])
            else:
                if round(scores_1[t]/finish_scores[t][0],3)*100<100.00:
                    percentage.append([round(scores_1[t]/finish_scores[t][0],3)*100]) 
                else:
                    percentage.append([100.0]) 
        for l in range(len(percentage)):
            if len(interpretations_json[l])>1: 
                interp_rercentage.append([float(percentage[l][i]) for i in range(len(interpretations_name[l]))])
            else:
                interp_rercentage.append([float(percentage[l][0])])
        scales_json = [{"title": i.name} for i in Scale.objects.filter(id__in=scales_pk)]
        for i in range(len(interp_rercentage)):
            scales_json[i]['result'] = interpretations_json[i]
            if len(scales_json[i]['result'])> 1:
                for u in range(len(scales_json[i]['result'])):
                    scales_json[i]['result'][u]['percent'] = interp_rercentage[i][u]
            else:
                scales_json[i]['result'][0]['percent'] = interp_rercentage[i][0]
        return Response(scales_json, status=status.HTTP_200_OK)
       
class AttemptViewSet(ViewSet):
    
    schema = AttemptSchema()
    @action(detail=False, methods=['post'])
    def create_attempt(self, request):
        
        if 'attempt' not in request.data:
            serializer = AttemptSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif 'attempt' in request.data:
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
        queryset = Scale.objects.all()
        serializer = ScaleSerializer(queryset, many=True)
        return Response(serializer.data)
    
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


