from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_name = models.CharField(max_length=200, null=True)
    blog_link = models.CharField(max_length=1_000, null=True)
    published_at = models.DateField(null=True)
    excerpt = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.title} - {self.published_at}"
