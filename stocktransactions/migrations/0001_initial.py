# Generated by Django 3.1.7 on 2021-03-21 16:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stockreceipts', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StockTransactions',
            fields=[
                ('id', models.CharField(db_column='ID', default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('StockTransactiontype', models.IntegerField(choices=[(0, 'Sales'), (1, 'Purchases'), (2, 'sales return'), (3, 'purchases returns')], db_column='STOCKTRANSACTIONTYPE', default=1)),
                ('status', models.IntegerField(db_column='STATUS', default=0)),
                ('datenew', models.DateTimeField(db_column='DATENEW', default=datetime.datetime(2021, 3, 21, 18, 36, 53, 859419))),
                ('person', models.ForeignKey(db_column='PERSON', default=0, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'StockTransactions',
                'db_table': 'StockTransactions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='StockTransactionlines',
            fields=[
                ('id', models.AutoField(db_column='ID', editable=False, primary_key=True, serialize=False)),
                ('units', models.FloatField(db_column='UNITS')),
                ('LinePrice', models.FloatField(db_column='LINEPRICE')),
                ('StockTransaction', models.ForeignKey(db_column='StockTransaction', on_delete=django.db.models.deletion.DO_NOTHING, to='stocktransactions.stocktransactions')),
                ('product', models.ForeignKey(blank=True, db_column='PRODUCT', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='stockreceipts.products')),
                ('stockdiary', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stockreceipts.stockdiary')),
            ],
            options={
                'db_table': 'StockTransactionLines',
                'managed': True,
                'unique_together': {('StockTransaction', 'id')},
            },
        ),
    ]
