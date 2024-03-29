# Generated by Django 3.0.2 on 2020-02-27 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0002_auto_20200226_1511'),
        ('user', '0003_auto_20200115_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikedTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='forum.Topic')),
            ],
        ),
    ]
