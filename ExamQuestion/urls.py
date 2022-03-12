from django.urls import path

from ExamQuestion.views import view_home, create_question

app_name = "exam"

urlpatterns = [
    path("", view_home, name="home"),
    path("create/", create_question, name="create")
]
