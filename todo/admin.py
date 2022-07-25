from django.contrib import admin
from .models import Todo
from django.contrib.auth.admin import UserAdmin

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_completed')
    search_fields = ('title', 'description', 'is_completed')
    list_per_page=25 
# Register your models here.
admin.site.register(Todo, TodoAdmin)

