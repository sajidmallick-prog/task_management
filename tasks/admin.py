from django.contrib import admin
from .models import Task

# 1. Define the custom settings first
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status')

# 2. Register the model AND the custom settings together
admin.site.register(Task, TaskAdmin)