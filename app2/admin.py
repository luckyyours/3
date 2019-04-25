from django.contrib import admin
from app2 import models

# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display = ["neirong"]
admin.site.register(models.book)