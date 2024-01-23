from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from django.contrib import messages
import datetime 

# Create your views here.

def base(request):
    return render(request, 'projectapp/base.html')

def time(request): 
    current_time = datetime.datetime.now()
    return render(request, 'projectapp/time.html', {'current_time':current_time})

def signup(request):
    if(request.method=="POST"):
        username = request.POST.get('name')
        password = request.POST.get('password')
        person = Account.objects.filter(username=username, password=password)
        if person.exists() == True: 
            messages.error(request, "Account already exists.", extra_tags='alert-danger')
            return redirect('signup')
        else: 
            Account.objects.create(username=username, password=password)
            messages.success(request, "Account created successfully.", extra_tags='alert-success')
            return redirect('login')
    else: 
        return render(request, 'projectapp/signup.html')

def login(request):
    if(request.method=="POST"):
        username = request.POST.get('name')
        password = request.POST.get('password')
        acc = Account.objects.filter(username=username, password=password)
        if acc.exists() == True:
            acc = get_object_or_404(Account, username=username, password=password)
            return redirect('homepage', pk=acc.pk)
        else: 
            messages.error(request, "Invalid Login", extra_tags='alert-danger')
            return redirect('login')
    else: 
        return render(request, 'projectapp/login.html')
    
def homepage(request):
    return render(request, 'projectapp/homepage.html')