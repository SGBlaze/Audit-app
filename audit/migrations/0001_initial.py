# Generated by Django 3.2.6 on 2022-08-04 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('referenceName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('referenceName', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('costPrice', models.FloatField()),
                ('subPrice', models.FloatField()),
                ('wholesalePrice', models.FloatField()),
                ('retailPrice', models.FloatField()),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='audit.company')),
            ],
        ),
    ]