# Generated by Django 3.2.6 on 2022-09-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0038_auto_20220902_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todaynewstock',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
