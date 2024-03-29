# Generated by Django 3.0.2 on 2020-02-27 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200114_1335'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_likedtopic'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
    ]
