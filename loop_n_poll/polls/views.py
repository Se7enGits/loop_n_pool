from django.db.models import F
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context — это словарь,
    # сопоставляющий имена переменных шаблона с объектами Python.
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)

# Старая версия функции:
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404('Question does not exist!')
#     return render(request, 'polls/detail.html', {'question': question})


# С шорткатом get_object_or_404():
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # request.POST is a dictionary-like object that lets you access
        # submitted data by key name. In this case, request.POST['choice']
        # returns the ID of the selected choice, as a string.
        # request.POST values are always strings.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        # selected_choice.votes += 1  # Если юзеры проголосуют одновременно,
        # им присвоится один и тот же номер...
        # Avoiding race conditions using F()
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,))
        )
