# Generated by Django 5.1.6 on 2025-03-28 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mssg_app', '0005_chatrooms_num_unread_mssgs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]
