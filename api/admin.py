from django.contrib import admin
from .models import *


class AnswerScaleInline(admin.StackedInline):
    model = AnswerScale
    extra = 0
    raw_id_fields = ('scale', 'answer', 'score')

class QuestionAnswerInline(admin.StackedInline):
    model = QuestionAnswer
    extra = 0
    raw_id_fields = ('question', 'answer') 

class CategoryTestInline(admin.StackedInline):
    model = CategoryTest
    extra = 0
    raw_id_fields = ('category', 'test') 

class TestSubtestInline(admin.StackedInline):
    model = TestSubtest
    extra = 0
    raw_id_fields = ('test', 'subtest') 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'queue',
        'status' 
    )
    search_fields = ('name', )
    list_filter = ('name', )
    fieldsets = (
        (None, {'fields': (
            'name',
            'queue',
            'status'
        )}),  
    )
    inlines = (CategoryTestInline,)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'queue',
        'category',
        'description_1',
        'description_2',
        'comment',
        'time_for_solution',
        'necessary_time',
        'mix_question',
        'status'
    )
    search_fields = ('name', )
    list_filter = ('status', 'category__name' )
    fieldsets = (
        (None, {'fields': (
            'name',
	        'queue',
            'description_1',
            'description_2',
            'comment',
            'time_for_solution',
            'necessary_time',
            'mix_question',
            'status',
            'category'
        )}),  
    )
    inlines = (TestSubtestInline,)

@admin.register(Subtest)
class SubtestAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'queue',
	    'test',
        'description_1',
        'description_2',
        'comment',
        'time_for_solution',
        'necessary_time',
        'mix_question',
        'status'
    )
    search_fields = ('name', 'test')
    list_filter = ('test__name', )
    fieldsets = (
        (None, {'fields': (
            'name',
            'queue',
            'description_1',
            'description_2',
            'comment',
            'time_for_solution',
            'necessary_time',
            'mix_question',
            'status',
            'test'
        )}),  
    )
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'queue',
        'subtest', 
        'type_question', 
        'obligatory', 
        'mix_question',
        'status'
    )
    search_fields = ('name', )
    list_filter = ('subtest__name','status', )
    fieldsets = (
        (None, {'fields': (
            'name',
            'queue',
            'type_question',
            'obligatory',
            'mix_question',
            'status',
            'subtest'
        )}),  
    )
    inlines = (QuestionAnswerInline,)
   
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'queue', 
	    'question',
        'right', 
        'scales'
    )
    search_fields = ('name', )
    list_filter = ('question__name', )
    fieldsets = (
        (None, {'fields': (
            'name',
            'queue',
            'right',
            'question'
    )}),  
    )
    inlines = (AnswerScaleInline,)
    def scales(self, obj):
        return obj.scale_answer.count()
    scales.short_description = 'Количество шкал'

@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'queue', 
        'status',
    )
    search_fields = ('name', )
    list_filter = ('status',)
    fieldsets = (
        (None, {'fields': (
            'name', 
            'queue', 
            'status',
    )}),
    )
    inlines = (AnswerScaleInline,)

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = (
	     'score',
    )
    search_fields = ('score',)
    fieldsets = (
        (None, {'fields': (
	     'score',
    )}),
    )
    inlines = (AnswerScaleInline,)

@admin.register(Interpretation)
class InterpretationsAdmin(admin.ModelAdmin):
    pass

""" @admin.register(Attemption)
class AttemptionsAdmin(admin.ModelAdmin):
    pass
 """
