from django.contrib import admin
from .models import ChatDB, GroupDB
# Register your models here.

admin.site.register(GroupDB)
admin.site.register(ChatDB)
