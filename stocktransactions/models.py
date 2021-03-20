import uuid

from django.db import models
from stockreceipts.models import Products
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime    

# Create your models here.
class StockTransactionlines(models.Model):
    id = models.AutoField( db_column='ID', primary_key=True, editable= False)   
    StockTransaction = models.ForeignKey('StockTransactions', models.DO_NOTHING, db_column='StockTransaction')  # Field name made lowercase.
    line = models.IntegerField(db_column='LINE',blank=True, null=True, editable=False)  # Field name made lowercase.
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='PRODUCT', blank=True, null=True)  # Field name made lowercase.
    units = models.FloatField(db_column='UNITS')  # Field name made lowercase.
    LinePrice = models.FloatField(db_column='LINEPRICE')  # Field name made lowercase.
    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        managed = True
        db_table = 'StockTransactionLINES'
        unique_together = (('StockTransaction', 'line'),)
        
class StockTransactions(models.Model):
    id = models.CharField(default=uuid.uuid4, db_column='ID', primary_key=True, max_length=255,editable= False)  
    
    
    SALES = 0
    PURCHASES = 1 
    SALES_RETURN = 2
    PURCHASE_RETURN = 3
    status_choices = [
    (SALES,'Sales'),
    (PURCHASES,'Purchases'),
    (SALES_RETURN,'sales return'),
    (PURCHASE_RETURN,'purchases returns'),
    ]

    StockTransactiontype = models.IntegerField(db_column='STOCKTRANSACTIONTYPE',choices=status_choices,default=PURCHASES)  # Field name made lowercase.
    person = models.ForeignKey(User, models.DO_NOTHING, db_column='PERSON',default=0)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', default=0)  # Field name made lowercase.  # Field name made lowercase.
    
    datenew = models.DateTimeField(db_column='DATENEW', default=datetime.now(), editable=True)  # Field name made lowercase.
    
    
    def __str__(self):
        return str(self.datenew) +"   "+ str(self.person) +"   "+str(self.status)
        pass
    class Meta:
        managed = True
        db_table = 'StockTransactions'
        verbose_name_plural='StockTransactions'
    


