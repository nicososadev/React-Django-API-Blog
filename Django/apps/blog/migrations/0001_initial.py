# Generated by Django 3.1.7 on 2021-02-28 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('content', models.CharField(max_length=250, verbose_name='Contenido')),
                ('slug', models.SlugField(max_length=250)),
                ('published', models.DateTimeField(auto_now_add=True, verbose_name='Publicado')),
                ('status', models.CharField(choices=[('published', 'Publicado'), ('notPublished', 'No Publicado')], default='notPublished', max_length=12, verbose_name='Estado')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'ordering': ('-published',),
            },
            managers=[
                ('publishedBlogs', django.db.models.manager.Manager()),
            ],
        ),
    ]
