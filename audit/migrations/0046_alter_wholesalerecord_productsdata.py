# Generated by Django 3.2.6 on 2022-09-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0045_auto_20220930_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesalerecord',
            name='productsData',
            field=models.JSONField(default={}),
        ),
    ]
