# Generated by Django 3.2.6 on 2022-09-01 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0034_auto_20220901_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='activedeliverystartrecord',
            name='salesId',
            field=models.FloatField(default=0),
        ),
    ]