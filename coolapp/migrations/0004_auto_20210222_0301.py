# Generated by Django 3.1.1 on 2021-02-22 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolapp', '0003_auto_20210220_0837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='participant',
            name='institution',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=models.CharField(max_length=50),
        ),
    ]
