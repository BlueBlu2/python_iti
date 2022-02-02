from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest,JsonResponse
from .models import MyUser
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    #return HttpResponse("<h1>welcome</h1>")
    if 'email' in request.session:
        return render(request, 'amazon/home.html')
    else:
        return redirect('login')

def home_name(request, name):
    return HttpResponse("<h1>welcome {} </h1>".format(name))

def contactus(request):
    if 'email' in request.session:
        return render(request, 'amazon/contactus.html')
    else:
        return redirect('login')

def aboutus(request):
    if 'email' in request.session:
        return render(request,'amazon/aboutus.html')
    else:
        return redirect('login')


def show_data(request):
    if 'email' in request.session:
        # return JsonResponse(request.GET)
        print(request.GET)
        return render(request, 'amazon/show_data.html', request.GET)
    else:
        return redirect('login')


def registerPage(request):
    context = {}
    if request.method == 'POST':
        name= request.POST['name']
        email=request.POST['email']
        password=request.POST['pass']
        user = MyUser.objects.filter(email=email)
        if not user:
            MyUser.objects.create(name=name,email=email,password=password)
            User.objects.create_user(username=name, password=password,email=email,is_staff=True)
            return redirect('login')
            #request.session['email'] = email
        else:
            context={'message':'user already exists'}
            return render(request,'accounts/register.html',context)
        return render(request, 'amazon/home.html')
    return render(request,'accounts/register.html',context)

def loginPage(request):
    context = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        #user = MyUser.objects.filter(email=email)
        if email and password:
            usr = MyUser.objects.filter(email=email, password=password)
            auth_usr = authenticate(username=usr[0].name,password=password,email=email)
            print(auth_usr)
            if usr:
                request.session['email'] = email
                login(request,auth_usr)
                return redirect('home')
        else:
            render(request, 'accounts/register.html', context)
    return render(request,'accounts/login.html',context)

def logout(request):
    # remove email from session
    request.session.pop('email')
    auth_logout(request)
    # go to login page "localhost:8000/"
    return redirect('login')

# def logout(request):
#     try:
#         # remove email from session
#         #del request.session['email']
#         request.session.pop('email')
#         auth_logout(request)
#
#     except KeyError:
#         pass
#     # go to home page "localhost:8000/"
#     return redirect('login')