from django.contrib import admin

from .models import Product # . is used because we are importing from same dir

admin.site.register(Product)