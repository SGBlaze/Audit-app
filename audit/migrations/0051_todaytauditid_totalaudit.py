# Generated by Django 3.2.6 on 2022-10-09 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('audit', '0050_auto_20221009_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='todayTauditId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditId', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TotalAudit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalAuditId', models.FloatField()),
                ('openingStock', models.JSONField(default=dict)),
                ('newStock', models.JSONField(default=dict)),
                ('closingStock', models.JSONField(default=dict)),
                ('driverDeliveryStockDetails', models.JSONField(default=dict)),
                ('shopAttendantDeliveryStockDetails', models.JSONField(default=dict)),
                ('expectedDriverDeliveryStockDetails', models.JSONField(default=dict)),
                ('expectedShopAttendantDeliveryStockDetails', models.JSONField(default=dict)),
                ('deliveryCustomersToTransfer', models.JSONField(default=dict)),
                ('invoiceIds', models.JSONField(default=dict)),
                ('allSubSales', models.JSONField(default=dict)),
                ('allWholesales', models.JSONField(default=dict)),
                ('allRetailSales', models.JSONField(default=dict)),
                ('shopCustomersToTransfer', models.JSONField(default=dict)),
                ('shopHandover', models.FloatField(default=0)),
                ('TotalDeliveryHandover', models.FloatField(default=0)),
                ('fullShopSalesAudit', models.JSONField(default=dict)),
                ('messages', models.JSONField(default=dict)),
                ('auditDate', models.DateTimeField(auto_now_add=True)),
                ('driver', models.ForeignKey(default='Driver Name not set', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drivername', to=settings.AUTH_USER_MODEL)),
                ('shopAttendant', models.ForeignKey(default='Shop Attendant name not Set', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shopattendantname', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]