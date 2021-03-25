from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .forms import userform
from django.contrib.auth.models import User
from .models import Register

def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return render(request,'Profile.html')
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')
def register_page(request):
    if request.method == "POST":
        name=request.POST.get('name')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')

        form = User.objects.create_user(first_name=name,last_name=lastname , email=email,username=username,password=password)

        form.save()
        return redirect('login')

    else:
        form = userform()
        return render(request,'register.html',{'form':form})
def logout_page(request):
    logout(request)
    return redirect('login')
def registration(request):
    if request.method =="GET":
        return render(request,'registration.html')
    else:
        name=request.POST.get('name')
        fname=request.POST.get('fname')
        address=request.POST.get('address')
        photo=request.POST.get('photo')
        phonenumber=request.POST.get('phonenumbe')
        email=request.POST.get('email')

        Register(
            name=name,
            fname=fname,
            address=address,
            photo=photo,
            phonenumber=phonenumber,
            email=email

        ).save()

        data=Register.objects.all()

        return render(request,'profile.html',{'data':data} )

def navbar(request):
    return render(request,'navbar.html')
def passwordreset(request):
    if request.method=="POST":
        email= request.POST.get('email')
        form= User.objects.email(email=email)
        form.save()
        return render(request,'password_reset.html', {'form':form})
    else:
        pass
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')



# Create your views here.
