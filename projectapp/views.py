from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Customer, Inventory, Product_Price, Order, Order_Inventory
from django.contrib import messages
from datetime import datetime 

# Create your views here.

def base(request):
    return render(request, 'projectapp/base.html')

def signup(request):
    if(request.method=="POST"):
        employee_id = request.POST.get('employeeid')
        employee_type = request.POST.get('employeetype')
        name = request.POST.get('name')
        password = request.POST.get('password')

        person = Account.objects.filter(Employee_ID=employee_id, 
                                        Employee_Type=employee_type, 
                                        Name=name, 
                                        Password=password)
        if person.exists() == True: 
            messages.error(request, "Account already exists.", extra_tags='alert-danger')
            return redirect('signup')
        else: 
            Account.objects.create(Employee_ID=employee_id, 
                                   Employee_Type=employee_type, 
                                   Name=name, 
                                   Password=password)
            messages.success(request, "Account created successfully.", extra_tags='alert-success')
            return redirect('login')
    else: 
        return render(request, 'projectapp/signup.html')

def login(request):
    if(request.method=="POST"):
        employee_id = request.POST.get('employeeid')
        password = request.POST.get('password')
        acc = Account.objects.filter(Employee_ID=employee_id, 
                                     Password=password)
        if acc.exists() == True:
            # acc = get_object_or_404(Account, Employee_ID=employee_id, Password=password)
            return redirect('homepage')
        else: 
            messages.error(request, "Invalid Login", extra_tags='alert-danger')
            return redirect('login')
    else: 
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
    orders = Order.objects.all()
    return render(request, 'projectapp/view_orders.html', {'orders':orders})

def view_customers(request): 
    customers = Customer.objects.all()
    return render(request, 'projectapp/view_customers.html', {'customers':customers})

def new_customer(request):
    if(request.method=="POST"):
        customer_type = request.POST.get('ordertype')
        company_name = request.POST.get('companyname')
        contact_name = request.POST.get('contactname')
        phone_number = request.POST.get('phonenumber')
        email = request.POST.get('email')
        customer = Customer.objects.filter(
                                           Customer_Type=customer_type, 
                                           Company_Name=company_name, 
                                           Primary_Contact_Name=contact_name, 
                                           Phone_Number=phone_number,
                                           Email=email
                                           ) 
        if customer.exists() == True: 
            messages.error(request, "Customer already exists.", extra_tags='alert-danger')
            return redirect('signup')
        else: 
            Customer.objects.create(
                                    Customer_Type=customer_type, 
                                    Company_Name=company_name, 
                                    Primary_Contact_Name=contact_name, 
                                    Phone_Number=phone_number,
                                    Email=email
                                    )
            messages.success(request, "Customer created successfully.", extra_tags='alert-success')
            return redirect('view_customers')
    else: 
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