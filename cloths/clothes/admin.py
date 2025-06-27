from django.contrib import admin

# Register your models here.
from .models import clothes,users

admin.site.register(clothes)
admin.site.register(users)