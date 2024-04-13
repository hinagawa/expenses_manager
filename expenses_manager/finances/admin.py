from django.contrib import admin
from .models import Category, Currency, Finances, Goals, Users

admin.site.register(Category)
admin.site.register(Currency)
admin.site.register(Finances)
admin.site.register(Goals)
admin.site.register(Users)

# Register your models here.
