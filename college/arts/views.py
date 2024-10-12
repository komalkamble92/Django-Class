from django.shortcuts import render
from arts.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from arts.forms import *



# Create your views here.
class Login(object):
    pass

def home(request):
    return HttpResponse("hiii,this is my dynamic web page")

def home2(request):
    context={'message':'Hello, this is a dynamic web page with a template!'}
    return render(request,'index.html',context)

def student_list(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})


def function_list(request):
    if request.method == 'GET':
        return HttpResponse('Student')
    else:
        return HttpResponse('invalid request method')


# def student_count(request):
#     students=Student.objects.all().count()
#     return render(request,'student_list.html',{'students':students})

def get_students(request):
    students = Student.objects.all()
    return render(request, 'students3.html', {'students': students})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'confirm_delete.html', {'student': student})



def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})
    