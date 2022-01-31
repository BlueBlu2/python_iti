from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest,JsonResponse
from .models import student
# Create your views here.


def create_stud(request):

    if 'email' in request.session:
        context = {}
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            stud = student.objects.filter(email=email)
            if not stud:
                student.objects.create(name=name, email=email)
                return redirect('home')
        else:
            context['msg'] = "Add"
            return render(request,'affairs/create_stud.html',context)
    else:
        return redirect('login')

def all_stud(request):
    if 'email' in request.session:
        context = {}
        if request.method == 'POST':
            name = request.POST['name']
            result = student.objects.filter(name__icontains=name)
            context['students'] = result
            return render(request,'affairs/all_studs.html',context)
        else:
            result = student.objects.all()
            context['students']= result
            return render(request,'affairs/all_studs.html',context)
    else:
        return redirect('login')

def delete_stud(request,id):
    if 'email' in request.session:
        student.objects.filter(id=id).delete()
        return redirect('allstudent')
    else:
        return redirect('login')

def update_stud(request,id):
    if 'email' in request.session:
        context={}
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            student.objects.filter(id = id).update(name=name, email=email)
            return redirect('allstudent')
        else:
            context['msg'] = 'Update'
            stud =student.objects.filter(id=id)
            context['student'] = stud
            return render(request, 'affairs/create_stud.html',context)
    else:
        return redirect('login')