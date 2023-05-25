# Generated by Django 4.1.5 on 2023-05-25 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ganancias.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Aportes",
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
            name="Concepto",
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
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Tipo Concepto",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TipoConcepto",
            fields=[
                (
                    "code",
                    models.CharField(
                        max_length=20,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Código Tipo",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Tipo Concepto",
                    ),
                ),
            ],
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
                ("periodo", models.DateField()),
                ("valor", models.FloatField(default=0.0)),
                (
                    "tope",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ganancias.tope"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Liquidacion",
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
                ("periodo", models.DateField()),
                ("payday", models.DateField()),
            ],
            options={
                "verbose_name_plural": "Liquidaciones",
                "ordering": ["payday"],
                "unique_together": {("periodo", "payday")},
            },
        ),
        migrations.CreateModel(
            name="Empresa",
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
                    "name",
                    models.CharField(
                        max_length=120,
                        validators=[ganancias.validators.validate_name],
                        verbose_name="Razon Social",
                    ),
                ),
                (
                    "cuit",
                    models.CharField(
                        max_length=11, validators=[ganancias.validators.validate_cuit]
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Empleado",
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
                ("leg", models.IntegerField()),
                (
                    "name",
                    models.CharField(
                        max_length=120,
                        validators=[ganancias.validators.validate_name],
                        verbose_name="Nombre",
                    ),
                ),
                (
                    "cuil",
                    models.CharField(
                        max_length=11, validators=[ganancias.validators.validate_cuil]
                    ),
                ),
                (
                    "empresa",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ganancias.empresa",
                    ),
                ),
            ],
            options={
                "ordering": ["empresa__name", "leg"],
                "unique_together": {("leg", "empresa")},
            },
        ),
        migrations.CreateModel(
            name="ConceptoLiquidado",
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
                ("importe", models.FloatField(default=0.0)),
                (
                    "concepto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ganancias.concepto",
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
        ),
        migrations.AddField(
            model_name="concepto",
            name="tipo_concepto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ganancias.tipoconcepto"
            ),
        ),
        migrations.CreateModel(
            name="AportesPorcentaje",
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
                ("valor", models.FloatField(default=0.0)),
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
                    "aporte",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ganancias.aportes",
                    ),
                ),
            ],
        ),
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
                    "informa_en_unidad",
                    models.BooleanField(
                        default=False, verbose_name="¿Informa en unidad?"
                    ),
                ),
                (
                    "es_pago_ac",
                    models.BooleanField(
                        default=False, verbose_name="¿Es pago a cuenta?"
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
                    "tope",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="ganancias.tope",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Deducciones",
                "unique_together": {("tipo", "codigo_siradig")},
            },
        ),
    ]
