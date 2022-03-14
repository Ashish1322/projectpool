

from ctypes import Union
from curses.ascii import HT
import random
from unicodedata import name
from wsgiref.util import request_uri
from xml.dom import HierarchyRequestErr
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout , login
from institutes.models import Projects,Institue
from email.message import EmailMessage
import smtplib
from django.contrib import messages

def validate_otp(request ,uid ):
    
    if(request.method == 'POST'):
        
        
    
        ins = Institue.objects.get(unique_id = uid)
    
        otp = request.POST['otp']
        
        # If the otp is succcess then show success message and redirect to a success page and in bakcend update the otp verified to true
        if(otp == ins.otp):
            ins.otpverified = True
            ins.save()
            return render(request,"projectpool/success.html")
        
        # If opt is Wrong Try Again
        messages.error(request,"Invalid OTP Please try Again")
        return render(request,"projectpool/signup-further.html", { 'id' :uid} )

    return render(request,"projectpool/signup-further.html", { 'id' :uid} )

# Initial Function to show on langidng page
def logoutuser(request):
    logout(request)
    return redirect("home")

def home(request):
    projects = Projects.objects.all()
    tags = []
   
    logos = [] # Empty Query set for institutes
  
    for proj in projects:
        tags.append(proj.tags.split(" "))
        a = Institue.objects.get(user = proj.user)
        # /media/Projects/bike_VKdrURt.jpeg
        logos.append( '/media/'+ str(a.logo))


    
    
        



    return render(request,"../templates/projectpool/index.html",{'projects' : projects , 'tags': tags , 'logos':logos})

def admin_view(request):

    # IF the user is Authenticated then show it's details and projects
    if(request.user.is_authenticated):
        institue = Institue.objects.get(user = request.user)
        projects = Projects.objects.filter(user = request.user)
        return render(request,"../templates/projectpool/admin.html" , {'projects': projects, 'institue':institue})
    
    return HttpResponse("Authenticated Url, Login Required")

    


# Function to handle University Login
def login_university(request):
    if(request.method == "POST"):
        password = request.POST['password']
        username = request.POST['username']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("adminview")
        else:
            return HttpResponse("Fail")
    
    return HttpResponse("Authenticated URL")

# Function to handle University Signup
def signup_university(request):
    if(request.method == "POST"):

        # Fetching the data from form
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        unid = request.POST['unid']
        logo = request.FILES['logo']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']

        # Checking for user of email already exists
        try:
            user = User.objects.get(email=email)
            return HttpResponse("An account with this email already exists, Please use diffrent email address.")
            

        except Exception as e:
            pass

        try:
            user = User.objects.get(username=username)
            return HttpResponse("User name already exists")
            

        except Exception as e:
            if(password!=confirmpassword):
                return HttpResponse("Password doesn't matches")
                
          
            user = User.objects.create_user(username=username,password=password,email=email,first_name = name)
             # Saving the user but now account is not activate and will be activated after confirming all the details of the university
            user.is_active = False
            user.save()

            b = random.randrange(123456,999999)

            insti = Institue.objects.create( name = name, unique_id = unid , logo = logo , user = user , city=city, state = state, country = country , otp = b)
            insti.save()

            # sending the otp on the mail
           
            a = "<h2> Your OTP for verification on ProjectHub is " + str(b) + "</h2> <br> <p> Kindly Use this otp to confirm your email <br> Regards,<br>Team ProjectHub" 
   
            msg = EmailMessage()
            msg['Subject'] = 'OTP Verification for ProjectHub'
            msg['From'] = 'a.m2001nov@gmail.com' 
            msg['To'] = email
            msg.set_content(a, subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('a.m2001nov@gmail.com', 'jnksljbwejcklqwc') 
                smtp.send_message(msg)
                
            # Once the otp is sent redirecting to fill otp detials
            return redirect("otp",insti.unique_id)
        
    
    return HttpResponse("Authenticated URL")

