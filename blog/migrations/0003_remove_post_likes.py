# Generated by Django 3.2 on 2022-07-06 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]