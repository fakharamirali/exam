from django.db import models


# Create your models here.
class TextQuestions(models.Model):
    question = models.TextField()
    response = models.TextField()
