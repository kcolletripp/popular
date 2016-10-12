from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic
from .models import Target, TargetWiki

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'search/index.html'
    context_object_name = 'latest_searches'

    def get_queryset(self):
        #Return the last 5 published questions. (not including future releases)
        return Target.objects.all().order_by('-target_name')[:5]
