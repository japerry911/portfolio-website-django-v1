# Generated by Django 4.1.4 on 2022-12-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_remove_post_categories_remove_post_excerpt_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="published_at",
            field=models.DateTimeField(null=True),
        ),
    ]
