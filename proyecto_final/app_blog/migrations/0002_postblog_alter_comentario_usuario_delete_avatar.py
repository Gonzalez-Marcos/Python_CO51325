# Generated by Django 4.1.7 on 2023-04-28 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes/')),
                ('text', models.TextField(max_length=200)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postBlog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]