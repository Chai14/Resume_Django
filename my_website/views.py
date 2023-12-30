from django.shortcuts import render
from resume.models import resume_education
from resume.models import resume_certificates
from resume.models import resume_projects

def home(request):
    resume_data_ed = resume_education.objects.all()
    resume_data_pro = resume_projects.objects.all()
    resume_data_certi  = resume_certificates.objects.all()
    data = {
        'resumedataed' : resume_data_ed,
        'resumedatapro' : resume_data_pro,
        'resumedatacerti' : resume_data_certi
        }
    return render(request, "home.html", data)
