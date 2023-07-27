from django.db.models import Count
from django.shortcuts import render, redirect
from questions.models import Question
from questions.forms import AddQuestionForm, EnterpriseForm


def question_form(request):
    """Обработка запроса подачи вопроса."""
    if request.method == 'POST':
        form_add_question = AddQuestionForm(request.POST)
        form_enterprise = EnterpriseForm(request.POST)
        if form_add_question.is_valid() and form_enterprise.is_valid():
            if not form_enterprise.cleaned_data["title"]:
                form_add_question.save()
            else:
                a = form_enterprise.save()
                b = form_add_question.save(commit=False)
                b.enterprise = a
                b.save()
            return redirect('table_of_questions')
    else:
        form_add_question = AddQuestionForm()
        form_enterprise = EnterpriseForm()
    context = {
        'form_enterprise': form_enterprise,
        'form_add_question': form_add_question,
    }
    return render(request, 'questions/question_form.html', context)


def table_of_questions(request):
    """Обработка запроса выдачи вопросов и статистики."""
    questions = Question.objects.all()
    stats = Question.objects.select_related(
        'enterprise__division').values(
        'enterprise__division__title',
        'enterprise__title').annotate(
        question_count=Count('id')
    )
    context = {
        'questions': questions,
        'stats': stats,
    }
    return render(request, 'questions/table_of_questions.html', context)
