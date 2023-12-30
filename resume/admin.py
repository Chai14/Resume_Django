from django.contrib import admin
from resume.models import resume_education
from resume.models import resume_certificates
from resume.models import resume_projects
class resume_edit1(admin.ModelAdmin):
    list_display1 = ('school_name', 'school_duration', 'school_score')
class resume_edit2(admin.ModelAdmin):
    list_display2 = ('project_name', 'project_duration','project_details')
class resume_edit3(admin.ModelAdmin):
    list_display3 = ('certi_name','certi_month','certi_details')

admin.site.register(resume_certificates, resume_edit3)
admin.site.register(resume_projects, resume_edit2)
admin.site.register(resume_education, resume_edit1)

# Register your models here.
