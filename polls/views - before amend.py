from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# from django.template import loader

from .models import Question

# request is an HttpRequest object.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template('polls/index.html')
    context = {"latest_question_list": latest_question_list}
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)  # syntax shortcut


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    # question = get_object_or_404(Question, pk=question_id) as shortcut alternative
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        """
            request.POST is a dictionary-like object that lets you access submitted data by key name.
            In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
            Note that Django also provides request.GET for accessing GET data in the same way – but we’re explicitly using request.POST in our code,
            to ensure that data is only altered via a POST call.
        """
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {"question": question, "error_message": "You didn't select a choice."},
        )
        """
            request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data.
            The above code checks for KeyError and redisplays the question form with an error message if choice isn’t given
        """
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
        """
        After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse.
        HttpResponseRedirect takes a single argument: the URL to which the user will be redirected.

        We are using the reverse() function in the HttpResponseRedirect constructor in this example.
        This function helps avoid having to hardcode a URL in the view function.
        It is given the name of the view that we want to pass control to and the variable portion of the URL pattern that points to that view.
        For example: '/polls/3/results/'
        """
