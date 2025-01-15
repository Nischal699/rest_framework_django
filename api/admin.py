from django.contrib import admin
from api.models import Task 

class taskAdmin(admin.ModelAdmin):
    list_display=('title','completed')
    
admin.site.register(Task,taskAdmin)