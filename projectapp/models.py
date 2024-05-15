from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

    # Name = models.CharField(max_length=255, null=False, default="")
    # Username 
    # Password = models.CharField(max_length=16, null=False, default="")
    # Employee_ID = models.AutoField(primary_key=True, max_length=6, null=False)

class Account(AbstractUser):
    Employee_Type = models.CharField(max_length=255, null=False, default="-")
    
    def get_employeetype(self):
        return self.Employee_Type
    

class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True, max_length=5, null=False)
    Customer_Type = models.CharField(max_length=255, null=False, default="")
    Company_Name = models.CharField(max_length=255, null=True, default="") 
    Primary_Contact_Name = models.CharField(max_length=255, null=False, default="")
    Phone_Number = models.CharField(max_length=255, null=False, default="")
    Email = models.EmailField(max_length=254, null=True)
    objects = models.Manager()

class Inventory(models.Model):
    Product_ID = models.AutoField(primary_key=True, max_length=6, null=False)
    Product_Name = models.CharField(max_length=255, null=False, default="")
    Date_Updated = models.DateField()
    Current_Quantity = models.IntegerField(null=False)
    Unit = models.CharField(max_length=255, null=False)
    Unit_Price = models.FloatField(null=False, default=0)
    Acquisition_Code = models.CharField(max_length=6, null=False)
    Warehouse_Location = models.CharField(max_length=255, null=False)
    Supplier = models.CharField(max_length=255, null=False)
    objects = models.Manager()

class Order(models.Model): 
    Order_Reference_Number = models.AutoField(max_length=7, primary_key=True, null=False)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Product_ID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    Order_Date = models.DateField(null=False)
    Customer_Name = models.CharField(max_length=255, null=False) 
    Order_Status = models.CharField(max_length=255, null=False, default="Pending Payment")
    Payment_Status = models.CharField(max_length=255, null=False, default="Pending")
    Order_Quantity = models.IntegerField(null=False)
    Revised_Order_Quantity = models.IntegerField(null=True)
    # Discount = models.FloatField(null=True, default=0)
    # Amount = models.FloatField(null=False)
    Total_Amount = models.FloatField(null=False)
    Note = models.CharField(max_length=255)
    objects = models.Manager()

class Discount(models.Model):
    Discount_ID = models.AutoField(primary_key=True)
    Product_ID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Order_Reference_Number = models.ForeignKey(Order, on_delete=models.CASCADE)
    Discount = models.FloatField(null=False, default=0)
    objects = models.Manager()

class Order_Inventory(models.Model):
    Order_Reference_Number = models.ForeignKey(Order, on_delete=models.CASCADE)
    Product_ID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    Product_Quantity = models.IntegerField(null=False, default=0)
    Revised_Order_Quantity = models.IntegerField(null=True, default=0)
    Amount = models.FloatField(null=False, default=0)
    objects = models.Manager()