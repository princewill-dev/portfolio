from django.shortcuts import render

from .models import Project, Skill


def index(request):
    """Render the portfolio landing page from database content."""
    context = {
        "projects": Project.objects.filter(is_published=True),
        "skills": Skill.objects.filter(is_active=True),
    }
    return render(request, "index.html", context)
