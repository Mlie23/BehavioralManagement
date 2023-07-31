from typing import Set
from django.contrib import admin
from .models import Teacher, Question, Answer, Student, Result, Form
from .models import Strengths, Locations, Settings, Triggers, Behaviors, Consequences, SettingStrategies, TriggerStrategies, BehaviorStrategies,ConsequenceStrategies
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

#### Special case for downloading data quickly
class AnswerResource(resources.ModelResource):
    class Meta:
        model = Answer


class AnswerAdmin(ImportExportModelAdmin):
    resource_class = AnswerResource


admin.site.register(Answer, AnswerAdmin)
####

#### Special case for downloading data quickly
class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question


class QuestionAdmin(ImportExportModelAdmin):
    resource_class = QuestionResource


admin.site.register(Question, QuestionAdmin)
####


for classes in [Teacher, Student, Result, Form, Strengths, Locations, Settings, Triggers, Behaviors, Consequences, SettingStrategies, TriggerStrategies, BehaviorStrategies, ConsequenceStrategies]:
    admin.site.register(classes)
