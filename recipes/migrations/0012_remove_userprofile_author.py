# Generated by Django 4.2.11 on 2024-04-04 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_userprofile_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='author',
        ),
    ]
