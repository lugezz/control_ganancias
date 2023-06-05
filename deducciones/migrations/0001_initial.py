# Generated by Django 4.1.5 on 2023-05-31 11:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("ganancias", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Deduccion",
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
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("DE", "deduccion"),
                            ("CF", "cargaFamilia"),
                            ("PC", "retPerPago"),
                            ("MA", "manual"),
                        ],
                        default="DE",
                        max_length=2,
                    ),
                ),
                (
                    "codigo_siradig",
                    models.CharField(max_length=20, verbose_name="Código Siradig"),
                ),
                ("name", models.CharField(max_length=120, verbose_name="Nombre")),
                (
                    "periodicidad",
                    models.CharField(
                        choices=[("AN", "Anual"), ("ME", "Mensual")],
                        default="ME",
                        max_length=2,
                    ),
                ),
                (
                    "validity_from",
                    models.DateField(
                        default=datetime.datetime(2000, 1, 1, 0, 0),
                        verbose_name="Vigencia desde",
                    ),
                ),
                (
                    "validity_to",
                    models.DateField(
                        default=datetime.datetime(2500, 12, 31, 0, 0),
                        verbose_name="Vigencia hasta",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Deducciones",
                "ordering": ["tipo", "codigo_siradig"],
            },
        ),
        migrations.CreateModel(
            name="RegAcceso",
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
                ("fecha", models.DateTimeField(auto_now_add=True)),
                (
                    "reg_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-fecha"],
            },
        ),
        migrations.CreateModel(
            name="Tope",
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
            ],
        ),
        migrations.CreateModel(
            name="TablaArt30",
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
                ("period", models.DateField(verbose_name="Periodo")),
                ("value", models.FloatField(default=0.0, verbose_name="Importe")),
                (
                    "deduccion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deducciones.deduccion",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Tabla Art. 30",
                "ordering": ["-period", "deduccion"],
            },
        ),
        migrations.CreateModel(
            name="Registro",
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
                ("cuil", models.BigIntegerField()),
                ("deduccion", models.CharField(max_length=50)),
                ("tipo", models.CharField(max_length=50)),
                ("dato1", models.CharField(max_length=50)),
                ("dato2", models.CharField(blank=True, max_length=50, null=True)),
                ("porc", models.CharField(blank=True, max_length=3, null=True)),
                (
                    "id_reg",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="registers",
                        to="deducciones.regacceso",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DeduccionEmpleado",
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
                (
                    "validity_from",
                    models.DateField(
                        blank=True, null=True, verbose_name="Vigencia desde"
                    ),
                ),
                (
                    "validity_to",
                    models.DateField(
                        blank=True, null=True, verbose_name="Vigencia hasta"
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        blank=True,
                        max_length=120,
                        null=True,
                        verbose_name="Nombre - Razón Social",
                    ),
                ),
                ("value", models.FloatField(default=0.0, verbose_name="Importe")),
                (
                    "deduccion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deducciones.deduccion",
                    ),
                ),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ganancias.empleado",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Deducciones Empleado",
                "ordering": ["empleado", "deduccion"],
            },
        ),
        migrations.AddField(
            model_name="deduccion",
            name="tope",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="deducciones.tope",
            ),
        ),
        migrations.CreateModel(
            name="TopeValor",
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
                ("period", models.DateField()),
                ("value", models.FloatField(default=0.0)),
                (
                    "tope",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="deducciones.tope",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Topes - Valores",
                "ordering": ["-period", "tope"],
                "unique_together": {("tope", "period")},
            },
        ),
        migrations.AlterUniqueTogether(
            name="deduccion",
            unique_together={("tipo", "codigo_siradig")},
        ),
    ]