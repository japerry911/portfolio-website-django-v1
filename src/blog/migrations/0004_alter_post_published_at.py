# Generated by Django 4.1.4 on 2022-12-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_published_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="published_at",
            field=models.DateField(null=True),
        ),
    ]
