
from pyexpat import model
from turtle import Turtle
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Projects(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250,default="")
    department = models.CharField(max_length=60,default="")
    tags = models.CharField(default="", max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to ='Projects/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title 

class Institue(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default="")
    unique_id = models.CharField(max_length=10,default="")
    logo = models.FileField(upload_to='Logos/')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    city = models.CharField(max_length=100,default="")
    state = models.CharField(max_length=200 , default="")
    country = models.CharField(max_length=200 , default="")
    otp = models.CharField(max_length=10,default="")
    otpverified = models.BooleanField(default=False)
    def __str__(self):
        return self.name 
    


    
