# Generated by Django 5.1.6 on 2025-03-23 02:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mssg_app', '0002_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='sent_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
