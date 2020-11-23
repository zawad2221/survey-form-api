from django.db import models


class Answer(models.Model):

    questionNumber = models.CharField(max_length=12)
    answer = models.CharField(max_length=12)

   
    

class FormData(models.Model):
    email = models.CharField(max_length=53)
    age = models.BigIntegerField()
    gender = models.CharField(max_length=11)
    height = models.CharField(max_length=11)
    weight = models.FloatField()
    answers = models.ManyToManyField('Answer')
    mark = models.BigIntegerField()

    def get_answer(self):
        return "\n".join(["(Q"+p.questionNumber+"**Answer="+p.answer+")" for p in self.answers.all()])

