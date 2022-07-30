from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Todo_list)
class Todo_listAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created', 'last_modified')

@admin.register(newstats)
class newstats(admin.ModelAdmin):
    pass
