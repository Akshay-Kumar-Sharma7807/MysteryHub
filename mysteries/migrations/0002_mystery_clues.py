# Generated by Django 4.1.5 on 2023-01-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysteries", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="mystery",
            name="clues",
            field=models.TextField(default="No clues"),
            preserve_default=False,
        ),
    ]
