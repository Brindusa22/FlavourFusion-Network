# Generated by Django 4.2.11 on 2024-03-19 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('total_time', models.CharField(max_length=50)),
                ('servings', models.PositiveIntegerField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('main_course', 'Main Course'), ('soup', 'Soup'), ('sides', 'Sides'), ('dessert', 'Dessert')], max_length=30)),
                ('cuisine', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]