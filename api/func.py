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
    true_user_answers = set(request.POST.values()) & set(all_rights_pk)
    true_user_answers_pk = [int(i) for i in true_user_answers]
    scales = [i.scales_id for i in answ if i.right == True]
    interpret = [x.name for x in Interpretations.objects.filter(
        scale_id__in=scales)]

    percentage = round(
        len(true_user_answers) / len(all_rights_pk), 3
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
    return interpret
