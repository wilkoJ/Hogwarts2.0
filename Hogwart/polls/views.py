from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Student

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    
    def get_queryset(self):
        return Student.objects.all()
"""
class DetailView(generic.DetailView):
    model = Student
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Student.objects.all()
"""
