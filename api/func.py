from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404
from .models import *


def get_test_result(request: WSGIRequest, test: Test, attemption: Attemption):

    # Фильтрация интерпретаций относительно шкалы        #
    def interp_obj(lst):
        return Interpretations.objects.filter(scale_id__in=lst)
    
    def answer_obj(lst):
        if isinstance(lst, list):
            return Answers.objects.filter(
                id__in=true_user_answers_pk,scales_id__in=list)
        else:
            return Answers.objects.filter(
                id__in=true_user_answers_pk,scales_id=lst)


    # Процесс получения и обработки ответов пользователя #
    questions = [subtest.questions.all()
                 for subtest in test.subtests.all()]
    answers = []
    for x in questions:
        for b in x:
            answers += [ans for ans in b.answers.all()]
    rights_answers_pk = [str(i.pk) for i in answers if i.right == True]
    true_user_answers = set(request.POST.values()) & set(rights_answers_pk)
    true_user_answers_pk = [int(i) for i in true_user_answers]
    scales_pk = [i.scales_id for i in Answers.objects.filter(
                    id__in=true_user_answers_pk)]
    

    # Формирование двух списков, которые позволяют        #
    # работать с ответами, у которых одинаковые шкалы, а  #
    # так же, с ответами, у которых шкала встречается     #
    # лишь один раз во всём тесте                         #
    similar_scales_pk = set()
    non_similar_scales_pk = []
    for i in scales_pk:
        if scales_pk.count(i) > 1:
            similar_scales_pk.add(i)
        if scales_pk.count(i) == 1:
            non_similar_scales_pk.append(i)


    # Работа с распределением баллов, нахождение одинаков #
    # ых шкал и суммирование соответственных баллов. Рабо #
    # та с соответствующими интерпретациями и нахождение  #
    # процентного соотношения                             #
    percentage = []
    scores =[]
    sum_score = []
    inter_name = []
    
    if len(non_similar_scales_pk) != 0:
        scores += [
            i.score for i in answer_obj(non_similar_scales_pk)]
        fin_scores = [
            i.finish_score for i in interp_obj(non_similar_scales_pk)]
        inter_name += [
            i.name for i in interp_obj(non_similar_scales_pk)]
        for i in range(len(non_similar_scales_pk)):
            percentage.append(round(scores[i] / fin_scores[i], 3) * 100)

    if len(similar_scales_pk) != 0:
        for x in similar_scales_pk:
            sum_score.append(sum([
                i.score for i in answer_obj(x)]))
        fin_scores = [
            i.finish_score for i in interp_obj(similar_scales_pk)]
        inter_name += [
            i.name for i in interp_obj(similar_scales_pk)]
        if len(fin_scores) == 1:
            percentage.append(round(sum(sum_score) / fin_scores[0], 3) * 100)
        else:
            for i in range(len(sum_score)):
                percentage.append(round(sum_score[i] / fin_scores[i], 3) * 100)

    """ if list(attemption) == []:
        Attemption.objects.create(
            number=1,
            user=request.user,
            test=test
        )
    else:
        for at in attemption:
            at.number += 1
            at.save(update_fields=['number']) """

    return  scores, sum_score, fin_scores, inter_name, percentage
