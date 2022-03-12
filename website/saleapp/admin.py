from django.contrib import admin

# Register your models here.
from .models import Sales,Fruits

admin.site.register(Sales)
admin.site.register(Fruits)
