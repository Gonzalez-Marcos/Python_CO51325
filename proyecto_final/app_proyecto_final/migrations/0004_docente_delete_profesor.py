# Generated by Django 4.1.7 on 2023-05-02 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto_final', '0003_sala_delete_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
