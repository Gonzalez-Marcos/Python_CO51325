# Generated by Django 4.1.7 on 2023-05-02 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto_final', '0002_alter_avatar_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]