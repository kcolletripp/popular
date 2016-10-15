from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from .models import Target, TargetWiki

from .forms import TargetForm

# Create your views here.

#class IndexView(generic.ListView):
#    template_name = 'search/index.html'
#    context_object_name = 'latest_searches'
#
#    def get_queryset(self):
#        #Return the last 5 published questions. (not including future releases)
#        return Target.objects.all().order_by('-target_name')[:5]

#class ResultsView(generic.DetailView):
#    model = Target
#    template_name = 'search/result.html'

def index(request):
    latest_searches = Target.objects.all().order_by('-target_name')[:5]
    form = TargetForm()
    context = {'latest_searches': latest_searches, 'form':form} #dictionary
    return render(request, 'search/index.html', context)


def result(request):
    context = {}
    if request.method == 'POST':
        form = TargetForm(request.POST)
        target = form.save()
        context['target'] = target #'key':value
    else:
        #GET, or first time request
        form = TargetForm()
    context['form'] = form
    return render(request, 'search/result.html', context)
