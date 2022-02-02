from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse, QueryDict
from .models import student, Track,Intake,Trainee
from django.views import View
from .forms import addTraineeForm,addTraineeModel
from django.views.generic import ListView, CreateView
# Create your views here.


# class trackeCreateView(CreateView):
#     model = Track
#     fields='__all__'

class Tracklist(ListView):
    model = Track


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
            stud =student.objects.filter(id=id)#get
            context['student'] = stud[0]
            return render(request, 'affairs/create_stud.html',context)
    else:
        return redirect('login')

class AddTrainee(View):
    form=addTraineeForm()
    context = {}
    context['form'] = form
    def get(self, request):
        return render(request,'affairs/add_trainee.html',self.context)
    def post(self, request):
        self.form=addTraineeForm(request.POST)
        if self.form.is_valid():
            print('hello')
            intake = Intake.objects.get(id=request.POST['intakeid'])
            track = Track.objects.get(id=request.POST['trackid'])
            Trainee.objects.create(name=request.POST['name'], email=request.POST['email'], intakeid=intake,trackid=track)
            print(Trainee.objects.all())
        else:
            print(self.form.errors)
        return render(request,'affairs/add_trainee.html',self.context)

class AddTraineeModelForm(View):
    form=addTraineeModel()
    context = {}
    context['form'] = form
    def get(self,request):
        return render(request, 'affairs/add_trainee.html', self.context)
    def post(self,request):
        intake = Intake.objects.get(id=request.POST['intakeid'])
        track = Track.objects.get(id=request.POST['trackid'])
        print(request.POST)
        Trainee.objects.create(name=request.POST['name'], email=request.POST['email'], intakeid=intake,trackid=track)
        return render(request, 'affairs/add_trainee.html', self.context)


# def AddTraineeFun(request):
#     form=addTraineeForm()
#     context = {}
#     context['form'] = form
#     if request.method == "GET":
#         print('hello form get')
#         return render(request,'affairs/add_trainee.html',context)
#     else:
#         form=addTraineeForm(request.POST)
#         if (form.is_valid()):
#             print('hello')
#             intake = Intake.objects.get(id=request.POST['intakeid'])
#             track = Track.objects.get(id=request.POST['trackid'])
#             Trainee.objects.create(name=request.POST['name'], email=request.POST['email'], intakeid=intake,trackid=track)
#             #print(Trainee.objects.all())
#         else:
#             print('error')
#             context['error']=form.errors
#         return render(request,'affairs/add_trainee.html',context)