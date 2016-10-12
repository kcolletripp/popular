from django.conf.urls import url

from . import views

app_name = 'search' #assigns namespace compare to app_name
urlpatterns = [
	#ex: /search/
    url(r'^$', views.IndexView.as_view(), name='index'),
]

