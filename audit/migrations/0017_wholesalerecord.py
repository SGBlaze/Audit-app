# Generated by Django 3.2.6 on 2022-08-12 15:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0016_auto_20220810_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='WholesaleRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('customerName', models.CharField(max_length=100)),
                ('productQuantity', models.IntegerField()),
                ('productPrice', models.FloatField()),
                ('productTotal', models.FloatField()),
                ('soldAt', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.products')),
            ],
        ),
    ]