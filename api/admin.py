from django.contrib import admin
from .models import *


class AnswerScaleInline(admin.StackedInline):
    model = AnswerScale
    extra = 0
    raw_id_fields = ('scale', 'answer')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'scale_count')
    search_fields = ('name', )
    fieldsets = (
        (None, {'fields': ('name','queue','right','question')}),  
    )
    inlines = (AnswerScaleInline,)

    def scale_count(self, obj):
        return obj.scale_answer.count()
    scale_count.short_description = 'Количество шкал'


@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    list_display = ('name', 'answer_count')
    search_fields = ('name', 'score')
    fieldsets = (
        (None, {'fields': ('name', 'queue', 'score', 'status')}),
    )
    inlines = (AnswerScaleInline,)
    def answer_count(self, obj):
        return obj.answer.count()
    answer_count.short_description = 'Количество ответов'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Interpretation)
class InterpretationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionssAdmin(admin.ModelAdmin):
    pass


@admin.register(Subtest)
class SubTestAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TestsAdmin(admin.ModelAdmin):
    pass


@admin.register(Attemption)
class AttemptionsAdmin(admin.ModelAdmin):
    pass
