# Generated by Django 3.1.7 on 2021-03-21 13:06

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stockreceipts', '__first__'),
        ('stocktransactions', '0011_auto_20210321_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocktransactionlines',
            name='id',
            field=models.AutoField(db_column='ID', default=1, editable=False, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stocktransactionlines',
            name='stockdiary',
            field=models.OneToOneField(db_column='stockdiary', default=uuid.UUID('9c77bc9f-d7d9-4979-8ccd-008e8d29f509'), null=True, on_delete=django.db.models.deletion.CASCADE, to='stockreceipts.stockdiary'),
        ),
        migrations.AlterField(
            model_name='stocktransactions',
            name='datenew',
            field=models.DateTimeField(db_column='DATENEW', default=datetime.datetime(2021, 3, 21, 15, 5, 58, 790689)),
        ),
        migrations.AlterUniqueTogether(
            name='stocktransactionlines',
            unique_together={('StockTransaction', 'id')},
        ),
        migrations.RemoveField(
            model_name='stocktransactionlines',
            name='ID',
        ),
    ]
