from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404
from .models import *


def get_test_result(request: WSGIRequest, test: Test, attemption: Attemption):
    def interp_obj(list):
        return Interpretations.objects.filter(scale_id__in=list)

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
    # так же, с ответами, у которых шкала встречается еди #
    # Формирование двух списков, которые позволяют работа #
    # Формирование двух списков, которые позволяют работа #
    # Формирование двух списков, которые позволяют работа #
    similar_scales_pk = set()
    non_similar_scales_pk = []
    for i in scales_pk:
        if scales_pk.count(i) > 1:
            similar_scales_pk.add(i)
        if scales_pk.count(i) == 1:
            non_similar_scales_pk.append(i)

    response = []
    scores =[]
    inter_name = []
    if len(non_similar_scales_pk) != 0:
        
        scores += [
            i.score for i in Answers.objects.filter
            (id__in=true_user_answers_pk,
             scales_id__in=non_similar_scales_pk)]
        fin_scores = [
            i.finish_score for i in interp_obj(non_similar_scales_pk)]
        inter_name += [
            i.name for i in interp_obj(non_similar_scales_pk)]
        for i in range(len(non_similar_scales_pk)):
            response.append(round(scores[i] / fin_scores[i], 3) * 100)

    if len(similar_scales_pk) != 0:
        sum_score = []
        for x in similar_scales_pk:
            sum_score.append(sum([i.score for i in Answers.objects.filter
                                  (id__in=true_user_answers_pk,
                                   scales_id=x)]))
        fin_scores = [i.finish_score for i in
                      Interpretations.objects.filter(
                          scale_id__in=similar_scales_pk)]
        inter_name += [i.name for i in
                       Interpretations.objects.filter(
                           scale_id__in=similar_scales_pk)]
        if len(fin_scores) == 1:
            response.append(round(sum(sum_score) / fin_scores[0], 3) * 100)
        else:
            for i in range(len(sum_score)):
                response.append(round(sum_score[i] / fin_scores[i], 3) * 100)

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

    return scores, sum_score, fin_scores, inter_name, response
