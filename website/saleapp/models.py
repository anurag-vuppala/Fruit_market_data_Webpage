from curses import flash
from tkinter.font import BOLD
from django.db import models
from django import forms
import datetime
# Create your models here.
sale_person = (
                ('Anna','Anna'),
                ('Bob','Bob'),
                ('Charlene','Charlene'),
                ('David','David')
)

customer_country = ( 
                    ('UK','UK'),
                    ('France','France'),
                    ('Germany','Germany'),
                    ('Netherlands','Netherlands'),
                    ('Spain','Spain')
                    )


class Fruits(models.Model):
    fruit = ( 
                    ('Apple','Apple'),
                    ('Pears','Pears'),
                    ('Strawberries','Strawberries'),
                    ('Banana','Banana')
                    
                    )
    fruit_name    =  models.CharField(max_length=12,choices=fruit, default='Select')
    
    def __str__(self):
        return self.fruit_name


class Sales(models.Model):
    Date             =  models.DateTimeField(auto_now_add=True, null=True)
    Sale_Person      =  models.CharField(max_length=10,choices=sale_person, default='Select',null=True)
    Customer_Name    =  models.CharField(max_length=25, null=True)
    Customer_Country =  models.CharField(max_length=12,choices=customer_country, default='Select',null=True)
    Desired_Fruit    =  models.ManyToManyField(Fruits)

    def __str__(self):
        return self.Customer_Name
    
