# Generated by Django 3.2.6 on 2022-09-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0044_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wholesalerecord',
            old_name='id',
            new_name='customerId',
        ),
        migrations.RemoveField(
            model_name='wholesalerecord',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wholesalerecord',
            name='productQuantity',
        ),
        migrations.AddField(
            model_name='wholesalerecord',
            name='amtFromCustomer',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='wholesalerecord',
            name='customerCredit',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='wholesalerecord',
            name='customerDebt',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='wholesalerecord',
            name='modeOfPayment',
            field=models.CharField(default='Cash', max_length=100),
        ),
        migrations.AddField(
            model_name='wholesalerecord',
            name='productValue',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='wholesalerecord',
            name='productsData',
            field=models.JSONField(default='no products'),
        ),
    ]
