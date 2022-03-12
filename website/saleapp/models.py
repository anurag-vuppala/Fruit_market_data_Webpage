from curses import flash
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
    Desired_Fruit    =  models.CharField(max_length=12,choices=fruit, default='Select', blank=False)
    def __str__(self):
        return self.Desired_Fruit


class Sales(models.Model):
    Date             =  models.DateField(default=datetime.date.today())
    Sale_Person      =  models.CharField(max_length=10,choices=sale_person, default='Select',blank=False)
    Customer_Name    =  models.CharField(max_length=25,blank=False)
    Customer_Country =  models.CharField(max_length=12,choices=customer_country, default='Select',blank=False)
    Desired_Fruit    =  models.ManyToManyField(Fruits)

    
    def clean_fruitform(self):
        field = ""
        for data in self.cleaned_data['flowers']:
            field += str(data)+","
        return field.lstrip(",")

    

class SalesForm(forms.ModelForm):
      class Meta:      
            model = Sales
            fields = '__all__'