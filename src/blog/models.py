from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_name = models.CharField(max_length=200, null=True)
    blog_link = models.CharField(max_length=1_000, null=True)
    published_at = models.DateField(null=True)
    excerpt = models.CharField(max_length=100, null=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image_size = models.CharField(max_length=6, default="15rem")

    def __str__(self):
        return f"{self.title} - {self.published_at}"

    def categories_as_list(self):
        return [x["name"] for x in self.categories.values()]
