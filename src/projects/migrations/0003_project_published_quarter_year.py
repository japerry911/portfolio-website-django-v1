# Generated by Django 4.1.4 on 2022-12-25 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_remove_project_image_project_github_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="published_quarter_year",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
