from django.shortcuts import get_object_or_404, render

from .models import Project, Skill


def index(request):
    """Render the portfolio landing page from database content."""
    context = {
        "projects": Project.objects.filter(is_published=True),
        "skills": Skill.objects.filter(is_active=True),
    }
    return render(request, "index.html", context)


def project_detail(request, slug):
    """Render the full detail page for a single project."""
    project = get_object_or_404(Project, slug=slug, is_published=True)
    context = {"project": project}
    return render(request, "project_detail.html", context)
