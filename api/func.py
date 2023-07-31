from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404
from .models import *


def get_test_result(request: WSGIRequest, test: Test, attemption: Attemption):
    all_obj = [subtest.questions.all()
               for subtest in test.subtests.all()]
    answ = []
    for x in all_obj: 
        for b in x: answ += [ans for ans in b.answers.all()]
    all_rights_pk = [str(i.pk) for i in answ if i.right == True]
    true_user_answers = set(request.POST.values()) & set(all_rights_pk)
    true_user_answers_pk = [int(i) for i in true_user_answers]
    ans_obj = [i.scales_id for i in Answers.objects.filter(id__in=true_user_answers_pk)]
    num_rep = []
    num = []
    for i in ans_obj:
        if ans_obj.count(i)>1:
            num_rep.append(i)
        if ans_obj.count(i) == 1:
            num.append(i)
    
    resp = sum(
        [i.score for i in Answers.objects.filter
            (id__in=true_user_answers_pk, scales_id__in=num_rep)]
    )
    resp_1 = [i.score for i in Answers.objects.filter
            (id__in=true_user_answers_pk, scales_id__in=num)]
    
    interp = Interpretations.objects.filter(scale_id__in = num_rep)
    percentage = round(
            resp / interp.finish_score, 3
        ) * 100

    percentage_1 = 0
    if len(num) != 0:
        interp_1 = Interpretations.objects.filter(scale_id__in = num)
        

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
  
    return 
