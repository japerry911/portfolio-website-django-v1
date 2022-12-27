from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="projects-page"),
    path("project/<slug:slug>", views.project_detail, name="project-detail-page"),
]
