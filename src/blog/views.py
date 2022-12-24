from django.shortcuts import render

from .models import Post


def index(request):
    all_posts = Post.objects.all().order_by("-published_at")
    return render(request, "blog.html", {"posts": all_posts})
