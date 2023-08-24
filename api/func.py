from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_list_or_404
from .models import *
#Мы подбираем интерпретацию, в зависимости от полученных баллов. То есть, сначала мы складываем все баллы за пройденный тест
#и раскидываем их по шкалам. Допустим:
#	1) 3 вопроса связанны с первой шкалой
#	2) Идем в таблицу ScaleInterpret, делаем фильтрацию по id 
#	3) Идем в таблицу Interpretation и определяем в каком диапазоне
#	   лежит сумма ответов условного юзера
def get_test_result(request: WSGIRequest, test: Test):
    true_user_answer = set(request.POST.values()) & set(
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
            answer_id__in=true_user_answer
        ).values_list(
            'scale_id', 
            flat=True
        )
    )
    response = [] 
    for i in scales_id:
        score = sum(list(Score.objects.filter(id__in = list(
                        AnswerScale.objects.filter(
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
                    scale_id=i).values_list(
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
            "score": score,
            "interpretations": list(
                Interpretation.objects.filter(
                    scale_id=i).values_list(
                    'text', 
                    flat=True
                )
            ),
            "fin_scores": list(
                Interpretation.objects.filter(
                    scale_id=i).values_list(
                    'finish_score', 
                    flat=True
                )
            ),
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
            at.save(update_fields=['number'])  
    return sum_score, fin_sum_scores, scores, fin_scores,  percentage, inter_name """