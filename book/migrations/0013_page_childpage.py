# Generated by Django 5.1.3 on 2024-11-25 04:49

import django.db.models.deletion
import django.utils.timezone
import froala_editor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0012_readinglist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('summary', froala_editor.fields.FroalaField(blank=True, null=True)),
                ('description', froala_editor.fields.FroalaField(blank=True, null=True)),
                ('meta_title', models.CharField(blank=True, max_length=200, null=True)),
                ('meta_keyword', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pages/')),
                ('status', models.CharField(choices=[('private', 'Private'), ('public', 'Public')], default='private', max_length=10)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='book.page')),
            ],
        ),
        migrations.CreateModel(
            name='ChildPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', froala_editor.fields.FroalaField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_pages', to='book.page')),
            ],
        ),
    ]
