# Generated by Django 3.0.2 on 2020-01-15 03:10

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='comments.Comment'),
        ),
    ]
