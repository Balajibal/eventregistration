# Generated by Django 3.1.1 on 2021-02-20 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coolapp', '0002_auto_20210219_1033'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='Participant',
        ),
    ]
