# Generated by Django 4.2.21 on 2025-05-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_draft',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
