from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Student, Course, House, Teacher

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    def get_queryset(self):
        return Student.objects.all()

class StudentIndexView(generic.DetailView):
    model = Student
    template_name = 'polls/student_index.html'
    
    def get_queryset(self):
        return Student.objects.all()

class StudentView(generic.DetailView):
    model = Student
    template_name = 'polls/student.html'
    def get_queryset(self):
        return Student.objects.all()

class OtherView(generic.DetailView):
    model = Student
    template_name = 'polls/other.html'
    def get_queryset(self):
        return Student.objects.all()

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def student_view(request):
    _id = RepresentsInt(request.POST.get('id', False))
    if (_id):
        student = get_object_or_404(Student, pk=request.POST.get('id', False))
    else:
        return render(request, 'polls/index.html', {
            'error_message': "Id must be an int.",
        })
    try:
        name = request.POST.get('name',False);
    except (KeyError, Choice.DoesNotExist):
# Redisplay the question voting form.
        return render(request, 'polls/index.html', {
            'student': student,
            'error_message': "Name isn't define.",
        })
    else:
        if (name == student.student_name):
            print("Name = %s  id = %d", name, student.student_id)
            return HttpResponseRedirect(reverse('polls:student_index', args=(student.student_id,)))
        return render(request, 'polls/index.html', {
            'error_message': "Name doesn't match the id.",
        })
