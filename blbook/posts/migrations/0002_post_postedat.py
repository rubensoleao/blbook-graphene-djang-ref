# Generated by Django 3.2.5 on 2021-07-03 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postedAt',
            field=models.DateField(default=datetime.datetime(2021, 7, 3, 19, 3, 46, 492051)),
        ),
    ]
