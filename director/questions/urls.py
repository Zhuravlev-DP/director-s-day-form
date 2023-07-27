from django.urls import path

from questions.views import table_of_questions, question_form


urlpatterns = [
    path('', question_form, name='question_form'),
    path(
        'table_of_questions/',
        table_of_questions,
        name='table_of_questions'
    ),
]
