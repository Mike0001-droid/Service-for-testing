from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_list_or_404
from .models import *

def get_test_result(request: WSGIRequest, test: Test):
    #TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
    """ def answer_obj(lst):
        if isinstance(lst, list):
            return AnswerScale.objects.filter(
                answer_id__in=true_user_answers,scale_id__in=lst)
        else:
            return AnswerScale.objects.filter(
                answer_id__in=true_user_answers,scale_id=lst) """
    
    """ def interp_obj(lst):
        return Interpretation.objects.filter(scale_id__in=lst) """
    #TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#   

    true_user_answers = set(request.POST.values()) & set(str(x) for x in Question.objects.filter(status="Опубликовано", 
    subtest_id__in = test.subtests.values_list('id', flat=True)).values_list('answers', flat=True))
    
    scales_pk = list(AnswerScale.objects.filter(
        answer_id__in=true_user_answers).values_list('scale_id', flat=True))
    
    similar_scales_pk = set()
    non_similar_scales_pk = []
    for i in scales_pk:
        if scales_pk.count(i) > 1:
            similar_scales_pk.add(i)
        if scales_pk.count(i) == 1:
            non_similar_scales_pk.append(i)  
    return 
    
    
    


    #TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
    """ interp_obj = list(ScaleInterpret.objects.filter(scale_id__in=similar_scales_pk).values_list('id', flat=True))
    fin_scores = list(Interpretation.objects.filter(id__in=interp_obj).values_list('id', flat=True))
    sum_score = []
    for x in similar_scales_pk:
        sum_score.append(sum([i.score.score for i in answer_obj(x)]))
    return interp_obj, fin_scores, sum_score, true_user_answers
    """
    #TODO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#










    
    
    """ percentage = []
    scores =[]
    sum_score = []
    inter_name = []
    fin_scores = []
    fin_sum_scores = []
    
    if len(non_similar_scales_pk) != 0:
        scores += [
            i.score.score for i in answer_obj(non_similar_scales_pk)]
        fin_scores += [
            i.finish_score for i in interp_obj(non_similar_scales_pk)]
        inter_name += [
            i.text for i in interp_obj(non_similar_scales_pk)]
        for i in range(len(non_similar_scales_pk)):
            percentage.append(round(scores[i] / fin_scores[i], 3) * 100)

    if len(similar_scales_pk) != 0:
        for x in similar_scales_pk:
            sum_score.append(sum([
                i.score.score for i in answer_obj(x)]))
        fin_sum_scores += [
            i.finish_score for i in interp_obj(similar_scales_pk)]
        inter_name += [
            i.text for i in interp_obj(similar_scales_pk)]
        if len(fin_sum_scores) == 1:
            percentage.append(round(sum(sum_score) / fin_sum_scores[0], 3) * 100)
        else:
            for i in range(len(sum_score)):
                percentage.append(round(sum_score[i] / fin_sum_scores[i], 3) * 100)  """
    
    #return f" Вы получили {sum_score} баллов из {fin_sum_scores} {similar_scales_pk}, {non_similar_scales_pk}, {scales_pk} scores, fin_scores, percentage, inter_name" 
    #return similar_scales_pk, non_similar_scales_pk, scales_pk






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