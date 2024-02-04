from django.shortcuts import render, redirect, get_object_or_404
from .models import Account
from django.contrib import messages
from datetime import datetime 

# Create your views here.

def base(request):
    return render(request, 'projectapp/base.html')

def current_time(request): 
    current_time = datetime.now().strftime('%H:%M:%S')
    return render(request, 'projectapp/base.html', {'current_time':current_time})

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
    #if(request.method=="POST"):
        #username = request.POST.get('name')
        #password = request.POST.get('password')
        #acc = Account.objects.filter(username=username, password=password)
        #if acc.exists() == True:
            #acc = get_object_or_404(Account, username=username, password=password)
            #return redirect('homepage', pk=acc.pk)
        #else: 
            #messages.error(request, "Invalid Login", extra_tags='alert-danger')
            #return redirect('login')
    #else: 
        #return render(request, 'projectapp/login.html')
    return render(request, 'projectapp/login.html')
    
def homepage(request):
    return render(request, 'projectapp/homepage.html')

def manage_account(request):
    return render(request, 'projectapp/manage_account.html')

def homepage_office(request):
    return render(request, 'projectapp/homepage_office.html')

def edit_account(request):
    return render(request, 'projectapp/edit_account.html')

def view_inventory(request):
    return render(request, 'projectapp/view_inventory.html')

def view_orders(request):
    return render(request, 'projectapp/view_orders.html')

def view_customers(request): 
    return render(request, 'projectapp/view_customers.html')

def new_customer(request):
    return render(request, 'projectapp/new_customer.html')

def edit_customer(request):
    return render(request, 'projectapp/edit_customer.html')

def create_customer_order(request):
    return render(request, 'projectapp/create_customer_order.html')

def edit_order(request):
    return render(request, 'projectapp/edit_order.html')

def customer_order(request):
    return render(request, 'projectapp/customer_order.html')

def add_products(request):
    return render(request, 'projectapp/add_products.html')

def edit_inventory(request): 
    return render(request, 'projectapp/edit_inventory.html')

def edit_inventory_warehouse(request): 
    return render(request, 'projectapp/edit_inventory_warehouse.html')

def view_orders_warehouse(request):
    return render(request, 'projectapp/view_orders_warehouse.html')

def customer_order_warehouse(request):
    return render(request, 'projectapp/customer_order_warehouse.html')

def view_inventory_warehouse(request): 
    return render(request, 'projectapp/view_inventory_warehouse.html')

def edit_order_warehouse(request):
    return render(request, 'projectapp/edit_order_warehouse.html')

def customer_order_owner(request):
    return render(request, 'projectapp/customer_order_owner.html')

def view_inventory_owner(request):
    return render(request, 'projectapp/view_inventory_owner.html')

def view_customers_owner(request):
    return render(request, 'projectapp/view_customers_owner.html')

def view_orders_owner(request):
    return render(request, 'projectapp/view_orders_owner.html')