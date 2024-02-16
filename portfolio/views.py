from django.shortcuts import render
from .models import Project, AboutMe, Contact, Experience, Skill,  Certification

def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_detail.html', {'project' : project})

def home(request):
    about_mes = AboutMe.objects.first()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    certifications = Certification.objects.all()
    context = {
        'about_mes': about_mes,
        'projects': projects,
        'experiences': experiences,
        'skills': skills,
        'certifications': certifications,
    }
    return render(request, 'home.html', context)

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

def contact(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})
