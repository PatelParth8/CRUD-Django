from django.contrib import admin
from .models import *

# Register your models here.
class showregi(admin.ModelAdmin):
    list_display = ['name', 'email', 'contact', 'password']

admin.site.register(Register, showregi)

class showadd(admin.ModelAdmin):
    list_display = ['cname', 'ccolor', 'cprice']

admin.site.register(Add, showadd)