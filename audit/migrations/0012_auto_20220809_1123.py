# Generated by Django 3.2.6 on 2022-08-09 10:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0011_auto_20220809_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closingstock',
            name='addedAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='closingstockhistory',
            name='addedAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
