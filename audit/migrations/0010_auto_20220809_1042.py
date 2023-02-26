# Generated by Django 3.2.6 on 2022-08-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0009_auto_20220809_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closingstock',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='closingstockhistory',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newstock',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newstockhistory',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='openingstock',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='openingstockhistory',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]