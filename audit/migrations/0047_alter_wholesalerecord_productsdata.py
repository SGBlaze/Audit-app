# Generated by Django 3.2.6 on 2022-09-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0046_alter_wholesalerecord_productsdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wholesalerecord',
            name='productsData',
            field=models.JSONField(default=dict),
        ),
    ]