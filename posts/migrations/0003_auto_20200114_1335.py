# Generated by Django 3.0.2 on 2020-01-14 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_points'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-points']},
        ),
    ]