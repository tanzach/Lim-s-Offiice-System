# Generated by Django 5.0.2 on 2024-02-22 16:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projectapp", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="Company_Type",
            new_name="Company_Name",
        ),
    ]