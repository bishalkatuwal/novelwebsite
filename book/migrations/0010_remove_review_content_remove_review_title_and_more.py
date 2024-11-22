# Generated by Django 5.1.3 on 2024-11-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_remove_novel_is_featured_remove_novel_is_popular_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='content',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.TextField(default='Add Comment'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(),
        ),
    ]
