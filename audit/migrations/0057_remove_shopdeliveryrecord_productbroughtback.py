# Generated by Django 3.2.6 on 2022-10-10 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0056_delete_shopdeliveryrecordhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopdeliveryrecord',
            name='productBroughtBack',
        ),
    ]