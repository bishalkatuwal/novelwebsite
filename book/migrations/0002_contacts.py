# Generated by Django 5.1.3 on 2024-11-18 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.PositiveIntegerField()),
                ('novel_name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('messages', models.TextField()),
            ],
        ),
    ]
