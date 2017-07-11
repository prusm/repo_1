from django.contrib import admin
from .models import Post #z models.py importuje klase post

admin.site.register(Post) #rejestruje model 
