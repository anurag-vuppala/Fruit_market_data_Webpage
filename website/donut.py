# library
import sqlite3
from tkinter import font
from tkinter.ttk import Style
from turtle import title
from typing import Text
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.tix import Select


    

con = sqlite3.connect("db.sqlite3")
data = pd.read_sql_query('SELECT saleapp_fruits.fruit_name, COUNT( saleapp_sales_Desired_Fruit.fruits_id ) AS quantity FROM saleapp_fruits INNER JOIN saleapp_sales_Desired_Fruit ON saleapp_sales_Desired_Fruit.fruits_id=saleapp_fruits.id GROUP BY saleapp_fruits.fruit_name',con)
print(data.quantity)


fruit_quantity=data.quantity
label = data.fruit_name
explode =  (0.02,0.02,0.02,0.02)


  
  
patches, text = plt.pie(fruit_quantity, labels=fruit_quantity, explode=explode, labeldistance=0.87)
plt.legend(patches, label,loc="center")
plt.axis('equal')

my_circle=plt.Circle( (0,0), 0.8, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)

plt.title(label="Count of requests among all customers, by fruit",fontsize=16)
plt.suptitle("Customer Demand",fontsize=24,y=1)

plt.show()