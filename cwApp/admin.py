from django.contrib import admin

# Register your models here.
from .models import BlogPost
#access for admin
admin.site.register(BlogPost)