# Generated by Django 4.0.3 on 2022-03-11 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saleapp', '0007_alter_sales_customer_name_alter_sales_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='Desired_Fruit',
        ),
    ]
