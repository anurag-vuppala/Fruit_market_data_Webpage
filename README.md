# Fruit_market_data_Webpage

This task is completed by only using the built-in Django models. The specific versions of modules used during this task can be found in the requirements.txt file.

Step-by-Step walkthrough:-
        -The first step is to create a virtual machine (fruitVM) using the command "python -m vevn fruitVM" for the Mac Terminal.
        -Django(4.0.3) was installed with the remaining requirements from the requirements.txt file.
        -Once Django and the environment are set up, I created a Django Project ( the command "Django-admin startproject <project_name>") 'fruitsite'. After running the required migrations, I created the superuser using the command "python manage.py createsuperuser" and ran the Django server using the command "python manage.py runserver." After the server starts running, I check the used superuser log-in details to log in to the admin page.
        - Next step is to create an app to build our input panel. This can be done with the command "python manage.py stratapp <app_name>"(saleapp)
        - From here onwards, I used VSCode to build the app. 
        - After the app is successfully created, we can see a new folder with the app name appear in the root directory.
        - Now I created a new class in models.py which will create a database table representing the required attributes, which will be used by the salesperson to enter data. A date has to be automated, I used Django's built-in feature "auto_now_add" which adds the current DateTime to the database table when entered. * *We can also use the DateTime module, which gives the current data and the flexibility to change the date while inserting values.* *
Initially, drop-down menus were used for the Sales person, customer_country, and desired_fruit. Later, to complete the ** challenging part**, ManytoManyField is used to enable multiple selections of fruits, and a separate SQLite database table is created.
        After completing the model. I registered the model in the admin.py after importing it. The last step is to add the model name into the settings.py file and add the app name into the "INSTALLED_APP" section. 
        - Now we are ready to make migrations and start the server.
        -Once we are in the admin panel, we can see our app "Sales" in it. From here, we can add the data to the database. This can be done using the terminal or the front-end model.
        
Donut:-
         Donut chart is created using the mathplotlib library and the connecting table generated by Django to connect our two modules. 
         Here we used SQL Command to extract data for the Pie chart using 'inner join' in SQL. The output is then converted into a Pandas dataframe containing the fruit name and ordered quantity.

Donut.py is a standalone file and, on running, will output the current order count, by fruit. 
         
         
         
       
       
External sources used [ Django Documentation and matplotlib Documentation ]
I used Django documentation to understand the workings of manytomanyfield and matplotlib to create the Donut chart.



For further improvement, we can create a separate front end using HTML and JavaScript. With this new front-end, we will have more flexibility with the layout of the form and be able to display the donut chart on the front end, showing live updates of the order.