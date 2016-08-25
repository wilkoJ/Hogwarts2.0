from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Student, Course, House, Teacher

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    
    def get_queryset(self):
        return Student.objects.all()

class StudentView(generic.DetailView):
    model = Student
    template_name = 'polls/student.html'
    def get_queryset(self):
        return Student.objects.all()

def student_view(request):
    student = get_object_or_404(Student, pk=request.POST['id'])
    try:
        name = request.POST['name']
    except (KeyError, Choice.DoesNotExist):
# Redisplay the question voting form.
        return render(request, 'polls/index.html', {
            'student': student,
            'error_message': "Name isn't define.",
        })
    else:
        if (name == student.student_name):
            return HttpResponseRedirect(reverse('polls:student', args=(student.student_id)))
        return render(request, 'polls/index.html', {
            'error_message': "Name doesn't match the id.",
        })
