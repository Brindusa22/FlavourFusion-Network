# Generated by Django 4.2.11 on 2024-04-01 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_remove_reciperating_average_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperating',
            name='comment',
            field=models.TextField(default='No comment available'),
            preserve_default=False,
        ),
    ]
