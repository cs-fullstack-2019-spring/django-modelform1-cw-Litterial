# Generated by Django 2.0.6 on 2019-02-27 21:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cwApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2019, 2, 27, 21, 55, 45, 113771, tzinfo=utc)),
        ),
    ]