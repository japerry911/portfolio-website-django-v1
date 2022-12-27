from django.db import models
from django.core.validators import MinLengthValidator


class TimelineEntry(models.Model):
    formatted_datetime = models.CharField(max_length=100)
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(50)])
    order_number = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.title} - {self.formatted_datetime}"


class Skill(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def excerpt_as_list(self):
        return self.excerpt.split(", ")
