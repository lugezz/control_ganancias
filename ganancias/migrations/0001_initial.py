# Generated by Django 4.1.5 on 2023-06-06 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ganancias.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("deducciones", "0001_initial"),
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
                    "tipo_concepto",
                    models.CharField(
                        choices=[
                            ("REM", "Remunerativo"),
                            ("NOREM", "No Remunerativo"),
                            ("APOR", "Aporte"),
                        ],
                        default="REM",
                        max_length=5,
                    ),
                ),
                (
                    "periodicidad",
                    models.CharField(
                        choices=[("AN", "Anual"), ("ME", "Mensual")],
                        default="ME",
                        max_length=2,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Nombre"
                    ),
                ),
                ("habitualidad", models.CharField(default="HA", max_length=2)),
                ("exento", models.BooleanField(default=False)),
                (
                    "others",
                    models.BooleanField(default=False, verbose_name="Otros Empleos"),
                ),
                ("extras", models.JSONField(default=dict)),
            ],
            options={
                "ordering": ["others", "exento", "tipo_concepto", "name"],
            },
        ),
        migrations.CreateModel(
            name="OtrosConceptos",
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
                    "concepto",
                    models.CharField(
                        choices=[("SICOSS", "Tope SICOSS"), ("EXBO", "Exención Bono")],
                        max_length=10,
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
                ("value", models.FloatField(default=0.0, verbose_name="Importe")),
            ],
            options={
                "verbose_name_plural": "Otros Conceptos",
                "ordering": ["concepto"],
            },
        ),
        migrations.CreateModel(
            name="TablaArt94",
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
                ("from_value", models.FloatField(default=0.0, verbose_name="Desde")),
                ("to_value", models.FloatField(default=0.0, verbose_name="Hasta")),
                (
                    "tax_percent",
                    models.FloatField(default=0.0, verbose_name="Porcentaje"),
                ),
                ("tax_fixed", models.FloatField(default=0.0, verbose_name="Fijo")),
            ],
            options={
                "verbose_name_plural": "Tabla Art. 94",
                "ordering": ["-period", "from_value"],
            },
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
                ("period", models.DateField()),
                ("payday", models.DateField()),
            ],
            options={
                "verbose_name_plural": "Liquidaciones",
                "ordering": ["payday"],
                "unique_together": {("period", "payday")},
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
                (
                    "take_sac",
                    models.CharField(
                        choices=[("AN", "Anual"), ("JD", "Junio - Diciembre")],
                        default="AN",
                        max_length=2,
                        verbose_name="Consideración SAC",
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
                ("jubilado", models.BooleanField(default=False)),
                (
                    "zona_patagonica",
                    models.BooleanField(default=False, verbose_name="Zona Patagónica"),
                ),
                (
                    "fecha_baja",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha de Baja"
                    ),
                ),
                (
                    "tope_35_anual",
                    models.BooleanField(
                        default=True, verbose_name="Tope Límite 35% Liq. Anual"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
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
            name="DeduccionPeriodo",
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
                ("amount", models.FloatField(default=0.0)),
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
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=120,
                        null=True,
                        verbose_name="Nombre - Razón Social",
                    ),
                ),
                ("amount", models.FloatField(default=0.0, verbose_name="Importe")),
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
                ("amount", models.FloatField(default=0.0)),
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
                (
                    "liquidacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ganancias.liquidacion",
                    ),
                ),
            ],
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
            name="AporteLiquidado",
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
                ("amount", models.FloatField(default=0.0)),
                (
                    "aporte",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ganancias.aportes",
                    ),
                ),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ganancias.empleado",
                    ),
                ),
                (
                    "liquidacion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ganancias.liquidacion",
                    ),
                ),
            ],
        ),
    ]
