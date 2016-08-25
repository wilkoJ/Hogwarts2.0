from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.StudentView.as_view(), name='student'),
    url(r'^/student_view$', views.student_view, name='student_view'),
]
