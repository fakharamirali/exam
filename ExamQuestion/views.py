import random

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .forms import NewQuestionForm
from .models import TextQuestions


def view_home(request):
    questions = TextQuestions.objects.all()

    if not questions:
        return render(request, "exam/notQ.html")

    n = questions.count()
    index = random.randint(0, n - 1)

    context = {
        "Q": questions[index]
    }

    return render(request, 'exam/home.html', context)


@login_required
def create_question(request):
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse("exam:home"))

    context = {}

    if request.method == "GET":
        form = NewQuestionForm()

        context["form"] = form

    else:
        form = NewQuestionForm(request.POST)

        context["form"] = form

        if form.is_valid():
            form.save()
            return HttpResponse("Created")

    return render(request, "exam/new_question.html", context)
