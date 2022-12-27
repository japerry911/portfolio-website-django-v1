from django.shortcuts import get_object_or_404, render

from .models import Project


def index(request):
    all_projects = Project.objects.all().order_by("-published_quarter_year")
    return render(request, "projects.html", {"projects": all_projects})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "project-detail.html", {"project": project})
