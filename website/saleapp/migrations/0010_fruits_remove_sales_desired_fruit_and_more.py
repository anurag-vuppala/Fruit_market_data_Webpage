# Generated by Django 4.0.3 on 2022-03-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saleapp', '0009_sales_desired_fruit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Desired_Fruit', models.CharField(choices=[('Apple', 'Apple'), ('Pears', 'Pears'), ('Strawberries', 'Strawberries'), ('Banana', 'Banana')], default='Select', max_length=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='sales',
            name='Desired_Fruit',
        ),
        migrations.AddField(
            model_name='sales',
            name='Desired_Fruit',
            field=models.ManyToManyField(to='saleapp.fruits'),
        ),
    ]
