# Generated by Django 3.2.6 on 2022-08-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0012_auto_20220809_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openingstock',
            name='quantity',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='openingstockhistory',
            name='quantity',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
