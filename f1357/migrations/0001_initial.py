# Generated by Django 4.1.5 on 2023-06-06 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
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
                ("name", models.CharField(max_length=120, verbose_name="Nombre")),
                (
                    "descripcion",
                    models.CharField(
                        blank=True,
                        max_length=120,
                        null=True,
                        verbose_name="Descripción",
                    ),
                ),
                (
                    "parent_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="f1357.group",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="F1357Field",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=60,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Nombre",
                    ),
                ),
                (
                    "descripcion",
                    models.CharField(
                        blank=True,
                        max_length=120,
                        null=True,
                        verbose_name="Descripción",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="f1357.group",
                    ),
                ),
            ],
        ),
    ]
