# Generated by Django 3.2.6 on 2022-08-15 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0018_auto_20220815_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wholesalerecord',
            name='productPrice',
        ),
        migrations.RemoveField(
            model_name='wholesalerecord',
            name='productTotal',
        ),
    ]
