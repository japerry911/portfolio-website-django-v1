from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    technology = models.CharField(max_length=1_000)
    image_name = models.CharField(max_length=200, null=True)
    youtube_link = models.CharField(max_length=1_000, default="")
    github_link = models.CharField(max_length=1_000, default="")
    published_quarter_year = models.CharField(max_length=10, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.title} -> {self.published_quarter_year}"

    def technology_as_list(self):
        return self.technology.split("|||")
