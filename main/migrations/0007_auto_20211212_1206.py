# Generated by Django 2.2.5 on 2021-12-12 06:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_internship_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 12, 12, 6, 37, 771426), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
