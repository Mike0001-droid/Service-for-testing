from django.contrib import admin
from .models import *


""" @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass """


@admin.register(Interpretations)
class InterpretationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Scales)
class ScalesAdmin(admin.ModelAdmin):
    pass


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    pass


@admin.register(Questions)
class QuestionssAdmin(admin.ModelAdmin):
    pass


@admin.register(Subtest)
class SubTestAdmin(admin.ModelAdmin):
    pass


@admin.register(Test)
class TastsAdmin(admin.ModelAdmin):
    pass


@admin.register(Attemption)
class AttemptionsAdmin(admin.ModelAdmin):
    pass
