from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404
from .models import *


def get_test_result(request: WSGIRequest, test: Test, attemption: Attemption):
    all_obj = [subtest.questions.all()
               for subtest in test.subtests.all()]
    answ = []
    for x in all_obj:
        for b in x:
            answ += [ans for ans in b.answers.all()]
    all_rights_pk = [str(i.pk) for i in answ if i.right == True]
    all_rights_scores = [i.score for i in answ if i.right == True]
    true_user_answers = set(request.POST.values()) & set(all_rights_pk)
    true_user_answers_pk = [int(i) for i in true_user_answers]
    ans_obj = [i.scales_id for i in Answers.objects.filter(id__in=true_user_answers_pk)]
    num_rep = 0
    num = 0
    for i in ans_obj:
        if ans_obj.count(i)!=0:
            num_rep = i
        if ans_obj.count(i) == 1:
            num = i
    resp = sum(
        [i.score for i in Answers.objects.filter
            (id__in=true_user_answers_pk, scales_id=num_rep)]
    )
    resp_1 = sum(
        [i.score for i in Answers.objects.filter
            (id__in=true_user_answers_pk, scales_id=num)]
    )
    interp = Interpretations.objects.get(scale_id = num_rep)
    percentage = round(
            resp / interp.finish_score, 3
        ) * 100
    percentage_1 = 0
    if num != 0:
        interp_1 = Interpretations.objects.get(scale_id = num)
        percentage_1 = round(
            resp_1 / interp_1.finish_score, 3
        ) * 100

    if list(attemption) == []:
        Attemption.objects.create(
            number=1,
            user=request.user,
            test=test
        )
    else:
        for at in attemption:
            at.number += 1
            at.save(update_fields=['number'])
  
    return percentage
