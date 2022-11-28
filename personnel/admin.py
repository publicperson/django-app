from django.contrib import admin
from .models import Personnel, Education, Experience, Skill, Project

# Register your models here.

class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('FirstName', 'LastName', 'Email',) 
    search_fields = ('firstname', 'lastname',)
    ordering = ('FirstName',)
    filter_horizontal = ('Skill',)
    
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('Title',) 
    search_fields = ('title',)
    ordering = ('-id',)
    
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('Company', 'Role',) 
    search_fields = ('company', 'role',)
    ordering = ('-id',)
    
class EducationAdmin(admin.ModelAdmin):
    list_display = ('Institution', 'Programme',) 
    search_fields = ('institution', 'programme',)
    ordering = ('-id',)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('Title','Start_Date','Link',) 
    search_fields = ('title','start_Date',)
    ordering = ('Title',)


admin.site.register(Project,ProjectsAdmin)
admin.site.register(Personnel,PersonnelAdmin)
admin.site.register(Skill,SkillsAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Experience,ExperienceAdmin)



