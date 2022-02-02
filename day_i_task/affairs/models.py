from django.db import models

# Create your models here.
class student(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    intakeid=models.ForeignKey('Intake',on_delete=models.CASCADE)
    trackid=models.ForeignKey('Track',on_delete=models.CASCADE)

class Intake(models.Model):#ORM
    id=models.AutoField(primary_key=True)
    intakename=models.CharField(max_length=30)
    startdate=models.DateField()
    enddate=models.DateField()

class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)