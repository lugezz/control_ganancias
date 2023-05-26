# Generated by Django 4.1.5 on 2023-05-26 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ganancias", "0003_tablaart94_alter_concepto_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tablaart94",
            options={
                "ordering": ["-period", "from_value"],
                "verbose_name_plural": "Tabla Art. 94",
            },
        ),
        migrations.AlterField(
            model_name="tablaart94",
            name="from_value",
            field=models.FloatField(default=0.0, verbose_name="Desde"),
        ),
        migrations.AlterField(
            model_name="tablaart94",
            name="period",
            field=models.DateField(verbose_name="Periodo"),
        ),
        migrations.AlterField(
            model_name="tablaart94",
            name="tax_fixed",
            field=models.FloatField(default=0.0, verbose_name="Fijo"),
        ),
        migrations.AlterField(
            model_name="tablaart94",
            name="tax_percent",
            field=models.FloatField(default=0.0, verbose_name="Porcentaje"),
        ),
        migrations.AlterField(
            model_name="tablaart94",
            name="to_value",
            field=models.FloatField(default=0.0, verbose_name="Hasta"),
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
                        to="ganancias.deduccion",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Tabla Art. 30",
                "ordering": ["-period", "deduccion"],
            },
        ),
    ]
