# Generated by Django 3.1.4 on 2021-01-04 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0005_auto_20210104_0039'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='dew_point_tmp',
        ),
        migrations.RemoveField(
            model_name='bike',
            name='func_day',
        ),
    ]
