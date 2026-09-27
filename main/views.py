import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


from main.models import Experience, Skill, Project
from main.forms import ProjectForm, SkillForm, ExperienceForm


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "npm": "2506539523",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information System Student at Universitas Indonesia."
            "Interested in anything that relates to puzzle."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

# Experience 

def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
            "json",
            json_response.content.decode("utf-8"),
        )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "experience_list": experiences,
        "title_query": title_query,
        "category_query":category_query,
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Fathir Azka Dillafah",''
        "nickname": "Fathir",
        "form": form,
    }
    return render(request, "experience_form.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("main:show_experience")
            
    context = {
            "name": "Fathir Azka Dillafah",
            "nickname": "Fathir",
            "form": form,
            "experience": experience,
        }
    
    return render(request, "experience_form.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()

    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    if category_query:
        experiences = experiences.filter(category=category_query)

    experience_json = serializers.serialize("json", experiences)
    return HttpResponse(experience_json, content_type="application/json")

# Skills

def show_something(request):
    skills = Skill.objects.all()
    context = {
        "skill_list": skills,
    }

    return render(request, "name", context)

def add_stars(request, soemthing_id):
    something = get_object_or_404(Skill, pk=soemthing_id)
    if request.method == "POST":
        something.incremsmrm()
        return 


def show_skill(request):
    json_response = get_skill_json(request)
    skills = serializers.deserialize(
            "json",
            json_response.content.decode("utf-8"),
        )
    skills = [skill.object for skill in skills]
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()
    
    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "skill_list": skills,
        "title_query": title_query,
        "category_query": category_query,
    }
    return render(request, "skill.html", context)

def create_skill(request):
    form = SkillForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Skill baru berhasil ditambahkan!")
        return redirect("main:show_skill")

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "form": form,
    }
    return render(request, "skill_form.html", context)

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skill")

    return redirect("main:show_skill")

def update_skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    form = SkillForm(request.POST or None, instance=skill)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("main:show_skill")
            
    context = {
            "name": "Fathir Azka Dillafah",
            "nickname": "Fathir",
            "form": form,
            "skill": skill,
        }
    
    return render(request, "skill_form.html", context)

def get_skill_json(request):
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()
    skills = Skill.objects.all()

    if title_query:
        skills = skills.filter(title__icontains=title_query)

    if category_query:
        skills = skills.filter(category=category_query)

    skill_json = serializers.serialize("json", skills)
    return HttpResponse(skill_json, content_type="application/json")

# Projects

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "project_list": projects,
        "title_query": title_query,
        "category_query": category_query,
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects, use_natural_foreign_keys=True)
    return HttpResponse(projects_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("main:show_projects")
            
    context = {
            "name": "Fathir Azka Dillafah",
            "nickname": "Fathir",
            "form": form,
            "project": project,
        }
    
    return render(request, "projects_form.html", context)

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")


# Registers
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "form": form,
    }
    return render(request, "register.html", context)

# Login
def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "form": form,
    }
    return render(request, "login.html", context)

# Logout
def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

