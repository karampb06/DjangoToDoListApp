from django.contrib import admin

# Register your models here.
from tasks.models import Task  #imports the Task model class from the models.py file of the tasks app (Tasks folder)

admin.site.register(Task) #registers the Task model class to be visible on the Django admin interface

