# Generated by Django 5.1.4 on 2025-01-06 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_user_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
