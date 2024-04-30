from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Customer, Inventory, Product_Price, Order, Order_Inventory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.

def base(request):
    return render(request, 'projectapp/base.html')

def signup(request):
    if(request.method=="POST"):
        employee_id = request.POST.get('employeeid') # employee id will be username in Django authentication
        employee_type = request.POST.get('employeetype')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        person = Account.objects.filter(username=employee_id)
        if person.exists() == True: 
            messages.error(request, "Account already exists.", extra_tags='alert-danger')
            return redirect('signup')
        else: 
            if password == confirm_password: 
                Account.objects.create_user(username=employee_id, Employee_Type=employee_type, first_name=firstname, last_name=lastname, Email=email, password=password)
                messages.success(request, "Account created successfully.", extra_tags='alert-success')
                return redirect('manage_account')
            else: 
                messages.error(request, "Passwords do not match.", extra_tags='alert-danger')
                return redirect('signup')
    else: 
        return render(request, 'projectapp/signup.html')


def login_view(request):
    if(request.method=="POST"):
        employee_id = request.POST.get('employeeid')
        password = request.POST.get('password')
        user = authenticate(request, username=employee_id, password=password)

        if user is None: 
            messages.error(request, "Invalid Employee ID or Password", extra_tags='alert-danger')
            return redirect('login')
        else: 
            login(request, user)
            if user.Employee_Type == "Office Clerk": 
                return redirect('homepage_office') 
            else: 
                return redirect('homepage')
    else: 
        return render(request, 'projectapp/login.html')
    
def logout_view(request): 
    logout(request)
    return redirect('login')
    
def homepage(request):
    if request.user.is_authenticated:
        employee_type = request.user.Employee_Type
        if request.user.Employee_Type == "Office Clerk":     
            return render(request, 'projectapp/homepage_office.html', {'employee_type':employee_type})
        else: 
            return render(request, 'projectapp/homepage.html', {'employee_type':employee_type})
    else:
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def manage_account(request):
    if request.user.is_authenticated:
        accounts = Account.objects.all()
        employee_type = request.user.Employee_Type
        return render(request, 'projectapp/manage_account.html', {'accounts':accounts, 'employee_type':employee_type})
    else:
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def homepage_office(request):
    if request.user.is_authenticated: 
        employee_type = request.user.Employee_Type 
        if request.user.Employee_Type == "Office Clerk": 
            return render(request, 'projectapp/homepage_office.html', {'employee_type':employee_type})
        else: 
            return render(request, 'projectapp/homepage.html', {'employee_type':employee_type})
    else: 
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def edit_account(request, pk):
    if request.user.is_authenticated: 
        edit_account = Account.objects.filter(pk=pk)
        employee_type = request.user.Employee_Type
        if(request.method == "POST"):
            employee_id = request.POST.get('employeeid')
            emp_type = request.POST.get('employeetype')
            fname = request.POST.get('firstname')
            lname = request.POST.get('lastname')
            email = request.POST.get('email')
            old_password = request.POST.get('oldpassword')
            new_password1 = request.POST.get('newpassword1')
            new_password2 = request.POST.get('newpassword2')
            if check_password(old_password, request.user.password):
                # Django password hashing not working when changing password. Need to fix. 
                if new_password1 == new_password2: 
                    Account.objects.filter(pk=pk).update(username=employee_id, Employee_Type=emp_type, first_name=fname, last_name=lname, email=email, password=new_password1)
                    Account.objects.get(pk=pk).set_password(new_password1)
                    edit_account.save()
                    messages.success(request, "Account updated successfully.", extra_tags='alert-success')
                    return redirect('manage_account')
                else: 
                    messages.error(request, "New Passwords do not match.", extra_tags='alert-danger')
                    return redirect('edit_account', pk=pk)
            else: 
                messages.error(request, "Incorrect Password", extra_tags='alert-danger')
                return redirect('edit_account', pk=pk)
        else: 
            return render(request, 'projectapp/edit_account.html', {'account':edit_account, 'employee_type':employee_type})
    else: 
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def view_inventory(request):
    if request.user.is_authenticated: 
        inventory = Inventory.objects.all()
        employee_type = request.user.Employee_Type
        if request.user.Employee_Type == "Warehouse Staff": 
            return render(request, 'projectapp/view_inventory_warehouse.html', {'inventory':inventory, 'employee_type':employee_type})
        else: 
            return render(request, 'projectapp/view_inventory.html', {'inventory':inventory, 'employee_type':employee_type})
    else: 
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def view_orders(request):
    if request.user.is_authenticated: 
        orders = Order.objects.all()
        employee_type = request.user.Employee_Type
        return render(request, 'projectapp/view_orders.html', {'orders':orders, 'employee_type':employee_type})
    else: 
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def view_customers(request): 
    if request.user.is_authenticated: 
        customers = Customer.objects.all()
        employee_type = request.user.Employee_Type
        return render(request, 'projectapp/view_customers.html', {'customers':customers, 'employee_type':employee_type})
    else: 
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def new_customer(request):
    if request.user.is_authenticated: 
        employee_type = request.user.Employee_Type
        if(request.method=="POST"):
            customer_type = request.POST.get('ordertype')
            company_name = request.POST.get('companyname')
            contact_name = request.POST.get('contactname')
            phone_number = request.POST.get('phonenumber')
            email = request.POST.get('email')

            # Checks if a customer with exactly the same inputs exists
            customer = Customer.objects.filter(Customer_Type=customer_type, Company_Name=company_name, Primary_Contact_Name=contact_name, Phone_Number=phone_number,Email=email) 
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
            return render(request, 'projectapp/new_customer.html', {'employee_type':employee_type})
    else: 
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')
    

def edit_customer(request, pk):
    if request.user.is_authenticated: 
        edit_customer = Customer.objects.filter(pk=pk)
        employee_type = request.user.Employee_Type
        if(request.method == "POST"): 
            customer_type =  request.POST.get('customertype')
            company_name = request.POST.get('companyname')
            primary_contact_name = request.POST.get('contactname')
            email = request.POST.get('email')
            phone_number = request.POST.get('phonenumber')
            Customer.objects.filter(pk=pk).update(Customer_Type=customer_type, Company_Name=company_name, Primary_Contact_Name=primary_contact_name, Email=email, Phone_Number=phone_number)
            return redirect('view_customers')
        else: 
            return render(request, 'projectapp/edit_customer.html', {'customer':edit_customer, 'employee_type':employee_type})
    else: 
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def delete_customer(request, pk):
    Customer.objects.filter(pk=pk).delete()
    return redirect('view_customers')

def create_customer_order(request):
    if request.user.is_authenticated: 
        all_customers = Customer.objects.all()
        all_products = Inventory.objects.all()
        employee_type = request.user.Employee_Type

        return render(request, 'projectapp/create_customer_order.html', {'customers':all_customers, 'products':all_products, 'employee_type':employee_type})
    else:
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def edit_order(request):
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/edit_order.html', {'employee_type':employee_type})

def customer_order(request):
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/customer_order.html', {'employee_type':employee_type})

def add_products(request):
    employee_type = request.user.Employee_Type
    if(request.method == "POST"):
        date_updated = request.POST.get('dateupdated')
        supplier_name = request.POST.get('suppliername')
        product_id = request.POST.get('productid')
        product_name = request.POST.get('productname')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        ac_code = request.POST.get('acquisitioncode')
        location = request.POST.get('warehouselocation')

        product = Inventory.objects.filter(Product_ID=product_id)
        if product.exists() == True: 
            messages.error(request, "Product already exists", extra_tags='alert-danger')
            return redirect('add_products')
        else: 
            Inventory.objects.create(Product_ID=product_id, Product_Name=product_name, Date_Updated=date_updated, Current_Quantity=quantity, Unit=unit, Acquisition_Code=ac_code, Warehouse_Location=location, Supplier=supplier_name)
            messages.success(request, "Product Added to Inventory", extra_tags='alert-success')
            return redirect('view_inventory')
    else:
        return render(request, 'projectapp/add_products.html', {'employee_type':employee_type})

def edit_inventory(request, pk): 
    if request.user.is_authenticated: 
        edit_inventory = Inventory.objects.filter(pk=pk)
        employee_type = request.user.Employee_Type
        if request.user.Employee_Type == "Warehouse Staff": 
            return render(request, 'projectapp/edit_inventory_warehouse.html', {'edit_inventory':edit_inventory, 'employee_type':employee_type})
        else: 
            if(request.method == "POST"): 
                date_updated = request.POST.get('dateupdated')
                supplier_name = request.POST.get('suppliername')
                product_id = request.POST.get('productid')
                product_name = request.POST.get('productname')
                quantity = request.POST.get('quantity')
                added_quantity = request.POST.get('addquantity')
                unit = request.POST.get('unit')
                unit_price = request.POST.get('unitprice')
                ac_code = request.POST.get('acquisitioncode')
                location = request.POST.get('warehouselocation')
                total_quantity = int(quantity) + int(added_quantity)
                Inventory.objects.filter(pk=pk).update(Product_ID=product_id, Product_Name=product_name, Date_Updated=date_updated, Current_Quantity=total_quantity, Unit=unit, Unit_Price=unit_price, Acquisition_Code=ac_code, Warehouse_Location=location, Supplier=supplier_name)
                return redirect('view_inventory')
            else: 
                return render(request, 'projectapp/edit_inventory.html', {'edit_inventory':edit_inventory, 'employee_type':employee_type})
    else:
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def delete_inventory(request, pk): 
    Inventory.objects.filter(pk=pk).delete()
    return redirect('view_inventory')
        
# Warehouse Functions 
def edit_inventory_warehouse(request, pk): 
    if request.user.is_authenticated: 
        edit_inventory = Inventory.objects.filter(pk=pk)
        employee_type = request.user.Employee_Type
        if request.user.Employee_Type == "Warehouse Staff":
            if(request.method == "POST"): 
                date_updated = request.POST.get('dateupdated')
                supplier_name = request.POST.get('suppliername')
                product_id = request.POST.get('productid')
                product_name = request.POST.get('productname')
                quantity = request.POST.get('quantity')
                added_quantity = request.POST.get('addquantity')
                unit = request.POST.get('unit')
                ac_code = request.POST.get('acquisitioncode')
                location = request.POST.get('warehouselocation')
                total_quantity = int(quantity) + int(added_quantity)
                Inventory.objects.filter(pk=pk).update(Product_ID=product_id, Product_Name=product_name, Date_Updated=date_updated, Current_Quantity=total_quantity, Unit=unit, Acquisition_Code=ac_code, Warehouse_Location=location, Supplier=supplier_name)
                return redirect('view_inventory')
            else: 
                return render(request, 'projectapp/edit_inventory_warehouse.html', {'edit_inventory':edit_inventory, 'employee_type':employee_type})
        else: 
            return render(request, 'projectapp/edit_inventory.html', {'edit_inventory':edit_inventory, 'employee_type':employee_type})
    else: 
        messages.error(request, "Login Required.", extra_tags='alert-danger')
        return redirect('login')

def view_orders_warehouse(request):
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/view_orders_warehouse.html', {'employee_type':employee_type})

def customer_order_warehouse(request):
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/customer_order_warehouse.html', {'employee_type':employee_type})

def view_inventory_warehouse(request): 
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/view_inventory_warehouse.html', {'employee_type':employee_type})

def edit_order_warehouse(request):
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/edit_order_warehouse.html', {'employee_type':employee_type})


# Owner Functions 
def customer_order_owner(request):
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/customer_order_owner.html', {'employee_type':employee_type})

def view_inventory_owner(request):
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/view_inventory_owner.html', {'employee_type':employee_type})

def view_customers_owner(request):
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/view_customers_owner.html', {'employee_type':employee_type})

def view_orders_owner(request):
    employee_type = request.user.Employee_Type
    return render(request, 'projectapp/view_orders_owner.html', {'employee_type':employee_type})


# HTMX Functions 
def fill_product_unit(request):
    product = request.GET.get('productname')
    product_unit = Inventory.objects.filter(pk=product)
    print(product)
    print(product_unit)
    return render(request, 'projectapp/product_unit.html', {'product_unit':product_unit})
    