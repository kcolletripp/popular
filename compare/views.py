from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

#only required if not using render
#from django.template import loader

from .models import Choice, Question


#def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    #output = ', '.join([q.question_text for q in latest_question_list])
#    template = loader.get_template('compare/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list} #dictionary
    return render(request, 'compare/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'compare/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'compare/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try: 
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form.
        return render(request, 'compare/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents double posting if they press back
        return HttpResponseRedirect(reverse('compare:results', args=(question.id,)))
