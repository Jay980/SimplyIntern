# Generated by Django 3.0 on 2021-11-05 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211016_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 20, 13, 4, 517771), verbose_name='date published'),
        ),
    ]
