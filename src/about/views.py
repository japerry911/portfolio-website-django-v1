from django.shortcuts import render

from .models import Skill, TimelineEntry


def index(request):
    timeline_entries = TimelineEntry.objects.all().order_by("order_number")
    skills = Skill.objects.all().order_by("title")

    return render(
        request,
        "about.html",
        {
            "timeline_entries": timeline_entries,
            "skills": skills,
        },
    )
