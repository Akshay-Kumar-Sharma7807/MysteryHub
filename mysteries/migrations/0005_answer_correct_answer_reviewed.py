# Generated by Django 4.1.5 on 2023-01-06 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysteries", "0004_mystery_solution"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="correct",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="answer",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
    ]
