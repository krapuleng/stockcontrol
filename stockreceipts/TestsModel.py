
class StockTransactionlines(models.Model):
    StockTransaction = models.OneToOneField('StockTransactions', models.DO_NOTHING, db_column='StockTransaction', primary_key=True)  # Field name made lowercase.
    line = models.IntegerField(db_column='LINE',blank=True, null=True)  # Field name made lowercase.
    product = models.ForeignKey(Products, models.DO_NOTHING, db_column='PRODUCT', blank=True, null=True)  # Field name made lowercase.
    units = models.FloatField(db_column='UNITS')  # Field name made lowercase.
    LinePrice = models.FloatField(db_column='LinePRICE')  # Field name made lowercase.
    def __str__(self):
        return f'{self.product.name}'

    class Meta:
        managed = True
        db_table = 'StockTransactionLINES'
        unique_together = (('StockTransaction', 'line'),)

class StockTransactionlinesInline(admin.TabularInline):
    model = StockTransactionlines

class StockTransactions(models.Model):
    id = models.CharField(default=uuid.uuid4, db_column='ID', primary_key=True, max_length=255,editable= False)  
    StockTransactiontype = models.IntegerField(db_column='StockTransactionTYPE')  # Field name made lowercase.
    StockTransactionid = models.IntegerField(db_column='StockTransactionID',default=0)  # Field name made lowercase.
    person = models.ForeignKey(People, models.DO_NOTHING, db_column='PERSON',default=0)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS')  # Field name made lowercase.  # Field name made lowercase.
    datenew = models.DateTimeField(db_column='DATENEW')  # Field name made lowercase.
    inlines = [
        StockTransactionlinesInline,
        ]
    def __str__(self):
        return str(self.id.datenew) +"   "+ str(self.person) +"   "+str(self.status)
        pass

    class Meta:
        managed = True
        db_table = 'StockTransactionS'
        verbose_name_plural='StockTransactionS'
