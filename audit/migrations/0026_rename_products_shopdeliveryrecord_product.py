# Generated by Django 3.2.6 on 2022-08-16 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0025_shopdeliveryrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shopdeliveryrecord',
            old_name='products',
            new_name='product',
        ),
    ]