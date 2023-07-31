from datetime import datetime
from sqlite3 import Date
from time import time, timezone
from xmlrpc.client import DateTime
from django.db import models
from django.contrib.auth import get_user_model


class Teacher(models.Model):
    user =           models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True,unique=True)
    first_name =     models.CharField(max_length=50)
    last_name =      models.CharField(max_length=50)
    school =         models.CharField(max_length=50)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        if(self.first_name and self.last_name):
            return f"{self.first_name} {self.last_name}"
        return "NULL"


# Create your models here.
class Question(models.Model):
    # can have duplicate
    # if empty then it is exclusively subquestion
    question_number = models.CharField(max_length=20, unique=True)
    text =            models.TextField()
    multiple_choice = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question_number}"


class Student(models.Model):
    first_name =    models.CharField(max_length=50)
    last_name =     models.CharField(max_length=50)
    student_id = models.CharField(max_length=50, default=0)
    teacher =       models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    date_of_birth = models.DateTimeField(null=True) 
    grade =         models.CharField(max_length=20, default ="Nan")
    gender =        models.CharField(max_length=20, default="Nan")
    IEP =           models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class Strategy(models.Model):
#     # planning with 8 boxes. Each will have its unique role in the finale.
#     text = models.TextField()
class Strengths (models.Model):
    strength = models.TextField(null=True, default='',blank='')
    def __str__(self):
        return self.strength[:25]
class Locations (models.Model):
    location = models.TextField(null=True, default='',blank='')
    def __str__(self):
        return self.location[:25]
class Settings (models.Model):
    setting = models.TextField(null=True, default='',blank='')
    class Meta:
        verbose_name = "Setting Event"
        verbose_name_plural = "Setting Events"
    def __str__(self):
        return self.setting[:25]
class Triggers (models.Model):
    trigger = models.TextField(null=True, default='',blank='')
    class Meta:
        verbose_name = "Triggering Antecedent"
        verbose_name_plural = "Triggering Antecedents"
    def __str__(self):
        return self.trigger[:25]
class Behaviors (models.Model):
    behavior = models.TextField(null=True, default='',blank='')
    def __str__(self):
        return self.behavior[:25]
class Consequences (models.Model):
    consequence = models.TextField(null=True, default='',blank='')
    class Meta:
        verbose_name = "Maintaining Consequence"
        verbose_name_plural = "Maintaining Consequences"
    def __str__(self):
        return self.consequence[:25]
class SettingStrategies (models.Model):
    setting_strategy = models.TextField(null=True, default='',blank='')
    def __str__(self):
        return self.setting_strategy[:25]  
    class Meta:
        verbose_name = "Setting Event Strategies"
        verbose_name_plural = "Setting Events Strategies"

class TriggerStrategies (models.Model):
    trigger_strategy = models.TextField(null=True, default='',blank='')
    question_number = models.CharField(max_length=20, default='',blank='')
    class Meta:
        verbose_name = "Antecedent strategy"
        verbose_name_plural = "Antecedent strategies"
    def __str__(self):
        return f"{self.question_number} {self.trigger_strategy}"

class BehaviorStrategies (models.Model):
    behavior_strategy = models.TextField(null=True, default='',blank='')
    question_number = models.CharField(max_length=20, default='',blank='')

    def __str__(self):
        return f"{self.question_number} {self.behavior_strategy}"

class ConsequenceStrategies (models.Model):
    consequence_strategy = models.TextField(null=True, default='',blank='')
    question_number = models.CharField(max_length=20, default='',blank='')

    def __str__(self):
        return f"{self.question_number} {self.consequence_strategy}"


class Answer(models.Model):
    text =                          models.TextField()
    next_question =                 models.ForeignKey(
        Question,
        on_delete=models.SET_NULL,
        related_name="next_question",
        verbose_name="Leads to Question:",
        null=True,
        blank=True,
    )
    question =                      models.ForeignKey(
        Question,
        on_delete=models.SET_NULL,
        related_name="this_question",
        verbose_name="Belongs to Question:",
        null=True,
    )
    # Strategies
    strength =                      models.ForeignKey(Strengths,on_delete=models.SET_NULL,null=True,blank=True)
    locations =                     models.ForeignKey(Locations, on_delete=models.SET_NULL,null=True,blank=True)
    setting =                       models.ForeignKey(Settings, on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Setting Event")
    trigger =                       models.ForeignKey(Triggers, on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Triggering Antecedent")
    behavior =                      models.ForeignKey(Behaviors, on_delete=models.SET_NULL,null=True,blank=True)
    consequence =                   models.ForeignKey(Consequences, on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Maintaining Consequence")
    setting_strategy =              models.ForeignKey(SettingStrategies, on_delete=models.SET_NULL,null=True,blank=True, verbose_name="Setting Event Strategy")
    trigger_strategy =              models.ForeignKey(TriggerStrategies, on_delete=models.SET_NULL,null=True,blank=True,verbose_name="Antecedent Strategy")
    behavior_strategy =             models.ForeignKey(BehaviorStrategies, on_delete=models.SET_NULL,null=True,blank=True)
    consequence_strategy =          models.ForeignKey(ConsequenceStrategies, on_delete=models.SET_NULL,null=True,blank=True)

    # Other
    is_other =                      models.BooleanField(default=False)


    OTHER_CHOICES                   = [('strength', 'strength'),
                                    ('locations', 'locations'),
                                    ('setting', 'setting'),
                                    ('trigger', 'trigger'),
                                    ('behavior', 'behavior'),
                                    ('consequence', 'consequence'),
                                    ('setting_strategy', 'setting_strategy'),
                                    ('trigger_strategy', 'trigger_strategy'),
                                    ('behavior_strategy', 'behavior_strategy'),
                                    ('consequence_strategy','consequence_strategy'),
                                    ]
    
    
    other_type = models.CharField(max_length = 20,choices=OTHER_CHOICES,null=True,default='strength')
    def __str__(self):
        return f"{self.question.question_number}., {self.question.text if self.question else 'None'}, {self.text}"


class Result(models.Model):
    student =  models.ForeignKey(Student, on_delete=models.CASCADE)
    # Go to answer 0 for custom input
    answer =   models.ForeignKey(Answer, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Custom_Strategy(models.Model):
    OTHER_CHOICES              = [('strength', 'strength'),
                                ('locations', 'locations'),
                                ('setting', 'setting'),
                                ('trigger', 'trigger'),
                                ('behavior', 'behavior'),
                                ('consequence', 'consequence'),
                                ('setting_strategy', 'setting_strategy'),
                                ('trigger_strategy', 'trigger_strategy'),
                                ('behavior_strategy', 'behavior_strategy'),
                                ('consequence_strategy','consequence_strategy'),
                                ]
    strategy_type = models.CharField(max_length = 20,choices=OTHER_CHOICES,null=True,default='strength')
    text = models.TextField(blank=True)
    def __str__(self):
        return str(f"{self.strategy_type}: {self.text}")



class Form(models.Model):
    date =    models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    answers = models.ManyToManyField(Answer)
    other_answer = models.ManyToManyField(Custom_Strategy)
    
    def __str__(self):
        return str(f"{self.student.first_name} {str(self.date)}")


