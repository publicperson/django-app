from django.contrib import admin
from .models import JobApplication, JobList

# Register your models here.

class JobListAdmin(admin.ModelAdmin):
    list_display = ('Title','Location','Salary',)
    ordering = ('id',)
    

admin.site.register(JobList, JobListAdmin)
admin.site.register(JobApplication)
