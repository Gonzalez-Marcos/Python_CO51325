# Generated by Django 4.1.7 on 2023-05-02 22:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto_final', '0005_alumno_delete_estudiante'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entregable',
        ),
        migrations.AlterField(
            model_name='alumno',
            name='dni',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999999), django.core.validators.MinValueValidator(10000000)]),
        ),
        migrations.AlterField(
            model_name='docente',
            name='telefono',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)]),
        ),
    ]
