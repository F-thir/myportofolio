import datetime

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core import serializers
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST


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
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "title_query": title_query,
        "category_query":category_query,
        "form": ExperienceForm(),
    }

    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.has_perm("main.add_experience"):
        raise PermissionDenied

    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.has_perm("main.delete_experience"):
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

@login_required(login_url="/login/")
def update_experience(request, experience_id):
    if not request.user.has_perm("main.change_experience"):
        raise PermissionDenied

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

@login_required(login_url="/login/")
def toggle_star_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()

    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    if category_query:
        experiences = experiences.filter(category=category_query)

    data = []
    for experience in experiences:
        starred_users = experience.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "thumbnail": experience.thumbnail,
                "is_ongoing": experience.is_ongoing,
                "started_at": experience.started_at,
                "ended_at": experience.ended_at,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@require_POST
def create_experience_ajax(request):
    if not request.user.has_perm("main.add_experience"):
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan experience."},
            status=403,
        )

    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience berhasil ditambahkan.", "pk": str(experience.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@require_POST
def update_experience_ajax(request, experience_id):
    if not request.user.has_perm("main.change_experience"):
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat mengedit experience."},
            status=403,
        )

    experience = get_object_or_404(Experience, id=experience_id)

    form = ExperienceForm(request.POST, instance=experience)

    if form.is_valid():
        experience = form.save()
        return JsonResponse(
            {"message": "Experience berhasil diperbarui.", "pk": str(experience.id)},
            status=200,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

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
    title_query = request.GET.get("title", "").strip()
    category_query = request.GET.get("category", "").strip()
    
    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "title_query": title_query,
        "category_query": category_query,
        "form": SkillForm(),
    }

    return render(request, "skill.html", context)

@login_required(login_url="/login/")
def create_skill(request):
    if not request.user.has_perm("main.add_skill"):
        raise PermissionDenied
    
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

@login_required(login_url="/login/")
def delete_skill(request, skill_id):
    if not request.user.has_perm("main.delete_skill"):
            raise PermissionDenied    
    
    skill = get_object_or_404(Skill, pk=skill_id)

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill berhasil dihapus!")
        return redirect("main:show_skill")

    return redirect("main:show_skill")

@login_required(login_url="/login/")
def update_skill(request, skill_id):
    if not request.user.has_perm("main.change_skill"):
        raise PermissionDenied
    
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

    data = []
    for skill in skills:

        data.append({
            "pk": str(skill.id),
            "fields": {
                "image": skill.image,
                "title": skill.title,
                "description": skill.description,
                "category": skill.category,
                "details": skill.details,
            }
        })

    return JsonResponse(data, safe=False)

@require_POST
def create_skill_ajax(request):
    if not request.user.has_perm("main.add_skill"):
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan skill."},
            status=403,
        )

    form = SkillForm(request.POST)
    if form.is_valid():
        skill = form.save()
        return JsonResponse(
            {"message": "Skill berhasil ditambahkan.", "pk": str(skill.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


# Projects

def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Fathir Azka Dillafah",
        "nickname": "Fathir",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.has_perm("main.add_project"):
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
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.has_perm("main.delete_project"):
        raise PermissionDenied

    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def update_project(request, project_id):
    if not request.user.has_perm("main.change_project"):
        raise PermissionDenied

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
def toggle_star_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")

@require_POST
def create_project_ajax(request):
    if not request.user.has_perm("main.add_project"):
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


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

