import uuid

from django.db import models
from stockreceipts.models import Products, Stockdiary,Locations,Stockcurrent
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.
class StockTransactionlines(models.Model):
    id = models.CharField(db_column='ID', primary_key=True,default=uuid.uuid4, max_length=255,editable= False)   
    StockTransaction = models.ForeignKey('StockTransactions', models.DO_NOTHING, db_column='StockTransaction')  # Field name made lowercase.
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='PRODUCT', blank=True, null=True)  # Field name made lowercase.
    units = models.FloatField(db_column='UNITS')  # Field name made lowercase.
    LinePrice = models.FloatField(db_column='LINEPRICE')  # Field name made lowercase.  
    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        managed = True
        db_table = 'StockTransactionLines'
        unique_together = (('StockTransaction', 'id'),)
        
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

@receiver(post_save, sender=StockTransactionlines)
def create_stocktransactionlines(sender, instance, created, **kwargs):
    if created:
        currentlocation = Locations.objects.get(id='0')
        costprice = instance.LinePrice/instance.units
        sellingprice=instance.product.pricesell

        Stockdiary.objects.create(id=instance.id,datenew=instance.StockTransaction.datenew,reason=1,product=instance.product,location=currentlocation,units=instance.units, price=sellingprice,costprice=costprice)
        
        stockcurrent = Stockcurrent.objects.get(product=instance.product.id)
        stockcurrent.units = stockcurrent.units + instance.units
        stockcurrent.save()
    else:
        print("The items already created")
        
@receiver(post_save, sender=StockTransactionlines)
def update_stockTransactionlines(sender, instance, created, **kwargs):
    try:
        if created==False:
            currentstockdiary = Stockdiary.objects.get(pk=instance.id)
            unitstoadd = instance.units - currentstockdiary.units            
            currentstockdiary.costprice = instance.LinePrice/instance.units
            currentstockdiary.units = instance.units
            currentstockdiary.save()  

            stockcurrent = Stockcurrent.objects.get(product=instance.product.id)
            stockcurrent.units = stockcurrent.units+unitstoadd
            stockcurrent.save()

    except Exception as e:
        print (e.message, type(e))

