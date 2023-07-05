from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def registration(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is taken')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is taken')
                return redirect('registration')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=fname,last_name=lname,email=email)
                user.save()
                print('register created')
                return redirect('login')

        else:
            messages.info(request,'password is not matching')
            return redirect('registration')


    return  render(request,'registration.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentiels')
            return redirect('login')
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')