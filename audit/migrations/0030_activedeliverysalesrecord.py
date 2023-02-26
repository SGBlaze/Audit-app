# Generated by Django 3.2.6 on 2022-08-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0029_activedeliverystartrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveDeliverySalesRecord',
            fields=[
                ('id', models.UUIDField(default=0, editable=False, primary_key=True, serialize=False, unique=True)),
                ('deliveryCustName', models.CharField(max_length=100)),
                ('deliveryProductData', models.JSONField()),
                ('productValue', models.FloatField()),
                ('modeOfPayment', models.CharField(max_length=100)),
                ('amtFromCustomer', models.FloatField()),
                ('customerDebt', models.FloatField()),
                ('customerCredit', models.FloatField()),
                ('purchasedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
