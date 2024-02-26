from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
admin.site.unregister(Group)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass

@admin.register(SeoScheme)
class SeoSchemeAdmin(admin.ModelAdmin):
    pass

@admin.register(Subtest)
class SubtestAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(PatternAnswer)
class PatternAnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(Scale)
class ScaleAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(AnswerForQuestion)
class AnswerForQuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Interpretation)
class InterpretationAdmin(admin.ModelAdmin):
    pass

@admin.register(Attemption)
class AttemptionAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
