# Generated by Django 5.1.3 on 2024-11-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_contacts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
