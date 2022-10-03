from email.policy import default
from unicodedata import decimal
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Product(models.Model): #inherit Product from models.Model
    title = models.CharField(max_length=120) #max_length=120
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places = 2, max_digits=100000)
    summary = models.TextField(blank=True, null = False) #default='This is cool'     #blank=False means its required and field is bold color. null=false deals with the database and its required.
    featured = models.BooleanField(default=True) #n null=True or  default=True
