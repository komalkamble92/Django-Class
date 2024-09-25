from django.shortcuts import render
from arts.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse


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

#def student_count(request):
    