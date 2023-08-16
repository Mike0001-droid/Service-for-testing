from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Interpretation)
class InterpretationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Scale)
class ScalesAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswersAdmin(admin.ModelAdmin):
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
