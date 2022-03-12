import sqlite3
import pandas as pd

con = sqlite3.connect('db.sqlite3')
c= con.cursor()

# data = c.execute('SELECT * FROM saleapp_sales_Desired_Fruit INNER JOIN saleapp_fruits ON saleapp_sales_Desired_Fruit.fruits_id=saleapp_fruits.id GROUP BY saleapp_fruits.Desired_Fruit').fetchall()

data = pd.read_sql_query('SELECT * FROM saleapp_sales_Desired_Fruit INNER JOIN saleapp_fruits ON saleapp_sales_Desired_Fruit.fruits_id=saleapp_fruits.id GROUP BY saleapp_fruits.Desired_Fruit',con)

c.close()
