# Generated by Django 5.0.2 on 2024-02-22 15:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "Employee_ID",
                    models.AutoField(max_length=6, primary_key=True, serialize=False),
                ),
                ("Employee_Type", models.CharField(default="", max_length=255)),
                ("Name", models.CharField(default="", max_length=255)),
                ("Password", models.CharField(default="", max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "Customer_ID",
                    models.AutoField(max_length=5, primary_key=True, serialize=False),
                ),
                ("Customer_Type", models.BooleanField()),
                (
                    "Company_Type",
                    models.CharField(default="", max_length=255, null=True),
                ),
                ("Primary_Contact_Name", models.CharField(default="", max_length=255)),
                ("Phone_Number", models.IntegerField()),
                ("Email", models.EmailField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Inventory",
            fields=[
                (
                    "Product_ID",
                    models.AutoField(max_length=6, primary_key=True, serialize=False),
                ),
                ("Product_Name", models.CharField(default="", max_length=255)),
                ("Date_Updated", models.DateField()),
                ("Current_Quantity", models.IntegerField()),
                ("Unit", models.CharField(max_length=255)),
                ("Acquisition_Code", models.CharField(max_length=6)),
                ("Warehouse_Location", models.CharField(max_length=255)),
                ("Supplier", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "Order_Reference_Number",
                    models.AutoField(max_length=7, primary_key=True, serialize=False),
                ),
                ("Order_Date", models.DateField()),
                ("Customer_Name", models.CharField(max_length=255)),
                ("Order_Status", models.CharField(max_length=255)),
                ("Payment_Status", models.CharField(max_length=255)),
                ("Unit_Price", models.FloatField()),
                ("Order_Quantity", models.IntegerField()),
                ("Revised_Order_Quantity", models.IntegerField()),
                ("Discount", models.IntegerField()),
                ("Amount", models.FloatField()),
                ("Total_Amount", models.FloatField()),
                ("Note", models.CharField(max_length=255)),
                (
                    "Customer_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectapp.customer",
                    ),
                ),
                (
                    "Product_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectapp.inventory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order_Inventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Order_Quantity", models.CharField(max_length=255)),
                (
                    "Order_Reference_Number",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectapp.order",
                    ),
                ),
                (
                    "Product_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectapp.inventory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product_Price",
            fields=[
                (
                    "Product_ID",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("Discount", models.IntegerField(max_length=3)),
                (
                    "Customer_ID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="projectapp.customer",
                    ),
                ),
            ],
        ),
    ]
