from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.StudentIndexView.as_view(), name='student_index'),
    url(r'^/teacher/(?P<pk>[0-9]+)/$', views.TeacherIndexView.as_view(), name='teacher_index'),
    url(r'^/course/(?P<pk>[0-9]+)$', views.CourseView.as_view(), name='course'),
    url(r'^/houses$', views.HouseView.as_view(), name='houses'),
    url(r'^/student/(?P<pk>[0-9]+)/$', views.StudentView.as_view(), name='student'),
    url(r'^/student_view$', views.student_view, name='student_view'),
    url(r'^/teacher_view$', views.teacher_view, name='teacher_view'),
    url(r'^/grade_student/(?P<teacher_id>[0-9]+)$', views.grade_student, name='grade_student'),
]
