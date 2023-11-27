from django.shortcuts import render, redirect
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import UserProfile
def registration(request):
    try:
        if request.method == 'POST':
            data = request.POST
            lastname = data.get('lastname')
            firstname = data.get('firstname')
            email = data.get('email')
            status = data.get('status')
            address = data.get('address')
            password = data.get('password')
            confirmpassword = data.get('confirmpassword')
            image = request.FILES.get('image')
            print(image)
            user = UserProfile.objects.filter(email= email)
            if user.exists():
               return render(request,'registration.html',{'message':'Username Already Taken'})

            if password == confirmpassword:
                UserProfile.objects.create(
                lastname = lastname,
                firstname= firstname,
                email=email,
                user_status=status,
                profile = image,
                password = password,
                confirmpassword = confirmpassword,
                address = address
                )
                return render(request,'registration.html',{'message':'SuccessFully Added'})
            else:
                return render(request,'registration.html',{'message':'Passwords is not matching'})
            return redirect("/registration")
        queryset = UserProfile.objects.all()
        context = {'files':queryset}
        return render(request,'registration.html',context)
    except Exception as e:
        print("Errorrrrrr:",e)
    return render(request,'error.html')

def login(request):
    try:
        if request.method =="POST":
            email =request.POST.get('email')
            password =request.POST.get('password')
            if UserProfile.objects.filter(email = email,password=password).exists():
                userinfo = UserProfile.objects.get(email = email)
                print(userinfo)
                return render(request,"dashboard.html",{'userinfo':userinfo})
            elif UserProfile.objects.filter(email=email).exists():
                return render(request,'login.html',{'message':'Invalid Password'})
            else:
                return render(request,'login.html',{'message':'User DoesNot Exist'})

        return render(request,"login.html")
    except Exception as e:
        print("Eroorrrrr:",e)


def dashboard(request):
    return render(request,'dashboard.html')