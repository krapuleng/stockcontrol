# Generated by Django 3.1.7 on 2021-03-21 12:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stockreceipts', '__first__'),
        ('stocktransactions', '0007_auto_20210321_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocktransactionlines',
            name='stockdiary',
            field=models.OneToOneField(db_column='stockdiary', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stockreceipts.stockdiary'),
        ),
        migrations.AlterField(
            model_name='stocktransactions',
            name='datenew',
            field=models.DateTimeField(db_column='DATENEW', default=datetime.datetime(2021, 3, 21, 14, 28, 13, 357351)),
        ),
    ]
