from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from app.models import Choice, Question
from django.utils import timezone

# Create your views here.
# Getting movies


def index(request):
    latest_question_list = Question.objects.filter(
        pub_date__lte=timezone.now()).order_by('-pub_date')[:10]
    context = {'latest_question_list': latest_question_list}
    # Loads templates
    return render(request, 'app/index.html', context)

# Show movie


def detail(request, question_id):

    try:
        question = Question.objects.filter(
            pub_date__lte=timezone.now()).get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'app/detail.html', {'question': question})

# Show results


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'app/results.html', {'question': question})

# Add favorite


def favorite(request, question_id):
    # print("POST: " + request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question form.
        return render(request, 'app/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.likes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app:results', args=(question.id,)))
