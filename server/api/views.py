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
from django.middleware.csrf import get_token
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt
from drf.settings import SECRET_KEY


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
        sub_id = [i['id'] for i in serializer.data['subtest']]
        quest_id = list(filter(None, list(Subtest.objects.filter(
            id__in=sub_id).values_list('questions', flat=True))))
        response = {'count': len(quest_id)}
        response.update(serializer.data)
        return Response(response)


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
    permission_classes = [IsAuthenticated]

    def list(self, request):
        decode = jwt.decode((request.META['HTTP_AUTHORIZATION'])[
                            7:], SECRET_KEY, algorithms=["HS256"])['user_id']
        queryset = Attemption.objects.filter(user=decode)
        data = []
        for i in set(queryset.values_list("test", flat=True)):

            data.append({
                "test_id": i,
                "test": get_object_or_404(Test, pk=i).name,
                "count": len(queryset.filter(test=i)),
                "attempts_id": [{"id": x.id, "created": Attemption.formatted_datetime(get_object_or_404(Attemption, pk=x.id))} for x in queryset.filter(test=i)]
            })
        return Response(data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Attemption.objects.filter(test=pk)
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
        scales_pk = list(set(attempt_id.answers.values_list(
            "scale_answer", flat=True)))
        s_f_scores = [list(Interpretation.objects.filter(scale=k).values_list(
            "start_score", "finish_score")) for k in scales_pk]

        inter_name = [list(Interpretation.objects.filter(
            scale=k).values_list("name", flat=True)) for k in scales_pk]

        scales_json = [{"title": i.name}
                       for i in Scale.objects.filter(id__in=scales_pk)]
        for i in range(len(scales_json)):
            scores_id = AnswerScale.objects.filter(scale=scales_pk[i]).values_list(
                "score", flat=True)
            scores = list(Score.objects.filter(
                id__in=scores_id).values_list("score", flat=True))
            if len(scores) > 1:
                fin_score = sum(scores)
            else:
                fin_score = sum(scores)*len(scores_id)

            scales_json[i].update({"fin_scores": fin_score})
            scales_json[i].update({"interpretations": inter_name[i]})
            scales_json[i].update({"s_f_cores": s_f_scores[i]})
        otvet = {"url": f"http://tests.flexidev.ru/#/attempt/{id}", "data": []}
        for i in range(len(scales_json)):
            otvet["data"].append(scales_json[i])
        return Response(otvet, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=['get'],
        url_path='user_attempt_by_id/(?P<id>[a-zA-Z0-9_.]+)',
        url_name='user-attempt-by-id',
    )
    def userattempt_by_id(self, request, id):
        decode = jwt.decode((request.META['HTTP_AUTHORIZATION'])[
                            7:], SECRET_KEY, algorithms=["HS256"])['user_id']
        queryset = Attemption.objects.filter(user=decode, test=id)
        data = []
        for i in queryset:
            data.append({
                "id": i.pk,
                "date": Attemption.formatted_datetime(i)
            })
        return Response(data, status=status.HTTP_200_OK)


class AttemptViewSet(ViewSet):
    permission_classes = [ViewTestNonDraft]
    schema = AttemptSchema()

    @action(detail=False, methods=['post'])
    def create_attempt(self, request):
        if 'attempt' not in request.data:
            if 'HTTP_AUTHORIZATION' in request.META:
                request.data['user'] = jwt.decode((request.META['HTTP_AUTHORIZATION'])[
                                                7:], SECRET_KEY, algorithms=["HS256"])['user_id']
            else:
                pass
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
            thing = [i.pk for i in list(
                chain(attempt.answers.all(), answers_id))]
            request.data['answers'] = thing
            try:
                instance = Attemption.objects.get(pk=pk)
            except:
                return Response({"error": "Object does not exists"})
            serializer = AttemptSerializer(
                data=request.data, instance=instance)
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
        queryset = Score.objects.filter(answer__in=attempt_id.answers.all())
        serializer = ScoreSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class InterpretationListViewSet(ViewSet):
    def list(self, request):
        queryset = Interpretation.objects.all()
        serializer = InterpretationSerializer(queryset, many=True)
        return Response(serializer.data)
