from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Students
from django.template import loader

# Create your views here.
def index(request):
    lastest_student_list = Students.objects.order_by('id')
    template = loader.get_template('students_app/index.html')
    context = {
        'latest_student_list' : lastest_student_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, id):
    try:
        student = Students.objects.get(pk=id)
    except Students.DoesNotExist:
        raise Http404("Student does not exist")
    return render(request, 'students_app/detail.html',{'student': student})