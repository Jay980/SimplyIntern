# Generated by Django 3.2.9 on 2021-11-24 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211124_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 21, 32, 48, 439766), verbose_name='date published'),
        ),
    ]
