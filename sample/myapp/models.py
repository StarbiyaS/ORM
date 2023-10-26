from django.db import models
from django.contrib import admin
class Player (models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    country=models.CharField(max_length=20)
    no_of_matches=models.IntegerField()
    date_of_birth=models.DateField()
# Create your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display=('name','age','country','no_of_matches','date_of_birth')