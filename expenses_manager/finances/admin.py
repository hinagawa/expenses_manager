from django.contrib import admin
from .models import Category, Finances, Goals, Users

admin.site.register(Category)
admin.site.register(Finances)
admin.site.register(Goals)

# Register your models here.
