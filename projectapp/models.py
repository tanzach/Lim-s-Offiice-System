from django.db import models

# Create your models here.

class Account(models.Model):
    Employee_ID = models.AutoField(primary_key=True, max_length=6, null=False)
    Employee_Type = models.CharField(max_length=255, null=False, default="")
    Name = models.CharField(max_length=255, null=False, default="")
    Password = models.CharField(max_length=16, null=False, default="")
    objects = models.Manager()
    
    def getName(self):
        return str(self.pk) + ": " + self.Name
    
    def getEmployee_Type(self):
        return str(self.pk) + ": " + self.Employee_Type
    
    def getEmployee_ID(self):
        return str(self.pk) + ": " + self.Employee_ID
    
    def getPassword(self):
        return str(self.pk) + ": " + self.Password
    
class Customer(models.Model):
    Customer_ID = models.AutoField(primary_key=True, max_length=5, null=False)
    Customer_Type = models.CharField(max_length=255, null=False, default="")
    Company_Name = models.CharField(max_length=255, null=True, default="") 
    Primary_Contact_Name = models.CharField(max_length=255, null=False, default="")
    Phone_Number = models.IntegerField(null=False)
    Email = models.EmailField(max_length=254, null=True)
    objects = models.Manager()

class Inventory(models.Model):
    Product_ID = models.AutoField(primary_key=True, max_length=6, null=False)
    Product_Name = models.CharField(max_length=255, null=False, default="")
    Date_Updated = models.DateField()
    Current_Quantity = models.IntegerField(null=False)
    Unit = models.CharField(max_length=255, null=False)
    Acquisition_Code = models.CharField(max_length=6, null=False)
    Warehouse_Location = models.CharField(max_length=255, null=False)
    Supplier = models.CharField(max_length=255, null=False)
    objects = models.Manager()

class Product_Price(models.Model):
    Product_ID = models.CharField(max_length=6, primary_key=True, null=False)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Discount = models.IntegerField(max_length=3, null=False)
    objects = models.Manager()

class Order(models.Model): 
    Order_Reference_Number = models.AutoField(max_length=7, primary_key=True, null=False)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Product_ID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    Order_Date = models.DateField(null=False)
    Customer_Name = models.CharField(max_length=255, null=False) 
    Order_Status = models.CharField(max_length=255, null=False)
    Payment_Status = models.CharField(max_length=255, null=False)
    Unit_Price = models.FloatField(null=False)
    Order_Quantity = models.IntegerField(null=False)
    Revised_Order_Quantity = models.IntegerField()
    Discount = models.IntegerField()
    Amount = models.FloatField(null=False)
    Total_Amount = models.FloatField(null=False)
    Note = models.CharField(max_length=255)
    objects = models.Manager()

class Order_Inventory(models.Model):
    Order_Reference_Number = models.ForeignKey(Order, on_delete=models.CASCADE)
    Product_ID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    Order_Quantity = models.CharField(max_length=255, null=False)
    objects = models.Manager()