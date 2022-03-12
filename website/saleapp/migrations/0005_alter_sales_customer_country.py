# Generated by Django 4.0.3 on 2022-03-10 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleapp', '0004_alter_sales_sale_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='Customer_Country',
            field=models.CharField(choices=[('UK', 'UK'), ('France', 'France'), ('Germany', 'Germany'), ('Netherlands', 'Netherlands'), ('Spain', 'Spain')], default='Select', max_length=12),
        ),
    ]