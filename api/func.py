from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import *
 
def get_test_result(request: WSGIRequest, test: Test):
    true_user_answer = set(request.POST.values()) & set(        #Извлечение ответов пользователя 
        str(x) for x in Question.objects.filter(
            status="Опубликовано",
            subtest_id__in = test.subtests.values_list(
                'id', 
                flat=True
            )
            ).values_list(
                'answers', 
                flat=True
            )
    )
    scales_id = set(AnswerScale.objects.filter(
            status="Опубликовано",                              #Извлечение шкал, которые используются
            answer_id__in=true_user_answer                      #в этом тесте
        ).values_list(
            'scale_id', 
            flat=True
        )
    )
    response = [] 
    for i in scales_id:
        score = sum(list(
            Score.objects.filter(id__in = list(    
                AnswerScale.objects.filter(
                    status="Опубликовано",
                    scale_id=i,
                    answer_id__in = true_user_answer,
                ).values_list(
                    'score_id', 
                    flat=True
                )
            )).values_list('score', flat=True)))
        percentage = [(round(x, 3) * 100) 
            for x in [
                score / i 
                for i in list(
                    Interpretation.objects.filter(
                    scale_id=i
                ).values_list(
                        'finish_score', 
                        flat=True
                    )
                )
            ]
        ]
        def processing(): 
            for i in range(len(percentage)):
                if percentage[i] > 100.00:
                    percentage[i] = 100.00
            return percentage
        response.append({
            "id": i,
            "scale_name": get_object_or_404(Scale, id=i).name,
            "score": score,
            "interpretations": list(
                Interpretation.objects.filter(
                    status="Опубликовано",
                    scale_id=i
                ).values_list(
                    'text', 
                    flat=True 
                )
            ),
            "fin_scores": list(
                Interpretation.objects.filter(
                    status="Опубликовано",
                    scale_id=i
                ).values_list(
                    'finish_score', 
                    flat=True
                )
            )[-1],
            "percentage": processing()
        })
    return response
 

    













    """ 
    if list(attemption) == []:
        Attemption.objects.create(
            number=1,
            user=request.user,
            test=test
        )
    else:
        for at in attemption:
            at.number += 1
            at.save(update_fields=['number']) """