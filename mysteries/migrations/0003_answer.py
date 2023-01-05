# Generated by Django 4.1.5 on 2023-01-05 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("mysteries", "0002_mystery_clues"),
    ]

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("answer", models.TextField()),
                (
                    "answered_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "mystery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mysteries.mystery",
                    ),
                ),
            ],
        ),
    ]