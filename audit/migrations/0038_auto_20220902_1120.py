# Generated by Django 3.2.6 on 2022-09-02 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0037_todaydeliverysalesrecord_todaydeliverystartrecord'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClosingStock',
            new_name='TodayClosingStock',
        ),
        migrations.RenameModel(
            old_name='NewStock',
            new_name='TodayNewStock',
        ),
        migrations.RenameModel(
            old_name='OpeningStock',
            new_name='TodayOpeningStock',
        ),
    ]
