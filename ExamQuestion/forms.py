from django import forms
from .models import TextQuestions


class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = TextQuestions
        fields = ["question", "response"]
