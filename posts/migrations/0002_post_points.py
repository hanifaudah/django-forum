# Generated by Django 3.0.2 on 2020-01-14 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]
