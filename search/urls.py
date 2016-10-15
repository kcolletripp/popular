from django.conf.urls import url

from . import views

app_name = 'search' #assigns namespace compare to app_name
urlpatterns = [
	#ex: /search/
    url(r'^$', views.index, name='index'),
    #ex: /polls/5/result/
    url(r'^result/$', views.result, name='result'),
]
