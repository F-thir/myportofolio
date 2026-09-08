from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Fathir Azka Dillafah",
        "npm": "2506539523",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Information System Student at Universitas Indonesia."
            "Interested in anything that relates to puzzle."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Fathir Azka Dillafah",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
