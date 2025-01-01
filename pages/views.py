from django.shortcuts import render
from .models import User
from .forms import *
# Create your views here.

def index(request):
    user_desc = User.objects.all()
    media_test = Testmedia.objects.all()
    return render(request, 'pages/index.html', {'user_desc': user_desc ,'media_test': media_test})

def login(request):
    name = request.POST.get('user_name')
    email = request.POST.get('user_email')
    password = request.POST.get('user_password')
    userData = User(name=name, email=email, password=password)
    # userData.save() 
    return render(request, 'pages/login.html',{"userData": LoginForm})

def testForm(request):
    test_form = test()
    
    return render(request, 'pages/testForm.html',{'test_form':test_form})