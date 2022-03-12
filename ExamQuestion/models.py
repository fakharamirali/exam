from django.db import models


# Create your models here.
class TextQuestions(models.Model):
    question = models.TextField(verbose_name="سوال")
    response = models.TextField(verbose_name="جواب")
