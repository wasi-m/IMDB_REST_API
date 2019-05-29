from django.contrib import admin

# Register your models here.

from .models import imdb_data

admin.site.register(imdb_data)