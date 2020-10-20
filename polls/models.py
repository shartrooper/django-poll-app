from django.db import models

import datetime

from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):  #Amend the method in models.py, so that it will only return True if the date is also in the past
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
'''
It’s important to add __str__() methods to your models, not only for your own convenience when dealing
with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.
'''
