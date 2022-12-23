from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    technology = models.CharField(max_length=1_000)
    image = models.FilePathField(path="/img")
