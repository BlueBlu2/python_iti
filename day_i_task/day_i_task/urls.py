"""day_i_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from amazon.views import home, contactus, aboutus, home_name, show_data, registerPage, loginPage,logout
from affairs.views import create_stud, all_stud,delete_stud,update_stud,AddTrainee, AddTraineeModelForm,Tracklist#trackeCreateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    #path('',home),
    path('home/<name>',home_name),
    path('logout',logout,name="logout"),
    path('contact/',contactus),
    path('about/',aboutus),
    path('showdata/',show_data),
    path('',loginPage,name="login"),
    path('regester/',registerPage,name="regester"),
    path('createstudent',create_stud,name='createstudent'),
    path('allstudents', all_stud, name='allstudent'),
    path('deletestud/<id>', delete_stud, name='deletestud'),
    path('updatestud/<id>', update_stud, name='updatestud'),
    path('AddTrainee', AddTrainee.as_view(), name='AddTrainee'),
    path('AddTraineeModel', AddTraineeModelForm.as_view(), name='AddTraineeModelForm'),
    path('Tracklist', Tracklist.as_view(), name='Tracklist'),
    #path('trackeCreateView', trackeCreateView.as_view(), name='trackeCreateView'),
    #path('AddTrainee', AddTraineeFun, name='AddTraineeFun'),
]
