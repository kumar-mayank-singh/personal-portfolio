from django.shortcuts import render


def contact(request):
    return render(request, 'contact/contact.html', {'contact': 'active'})

def education(request):
    return render(request, 'education/education.html', {'education': 'active'})

def home(request):
    return render(request,'home/home.html', {'home': 'active'})

def skills(request):
    return render(request, 'skills/skills.html',{'skills': 'active'})