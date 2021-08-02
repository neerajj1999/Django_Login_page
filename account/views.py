from re import I
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import  User, auth
from django.contrib import messages
from qrcode.main import QRCode
# Create your views here.


def index(request):
    return render(request, "hello.html")


def login(request):
    if request.method  =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request,user)
            return  redirect("form_page")
        else:
            messages.info(request,'invalid credentils')
            return  redirect('login')
    else:
        return render(request,"login.html")
def register(request):
    if request.method =='POST':
        first_name = request. POST['first_name']
        last_name = request. POST['last_name']
        username = request. POST['username']
        password1 = request. POST['password1']
        password2 = request. POST['password2']
        email = request. POST['email']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username AlreadyTaken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email AlreadyTaken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,
                                            email=email, first_name=first_name,last_name=last_name)


                user.save();
                messages.info(request,"user created")
                return  redirect('login')
        else:
            messages.info(request,'password not matching')
            return  redirect('register')

    else:
        return  render(request, 'register.html')


def form_page(request):
    objs = {"delhi" : 'delhi' , 
    # "Gurgaon" :'Gurgaon'
    }

    return render(request, 'form.html', objs)

