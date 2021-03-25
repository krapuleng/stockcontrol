from django.contrib import admin
from stockreceipts.models import Products
from stocktransactions.models import StockTransactions , StockTransactionlines
from stockreceipts.models import Products
import autocomplete_all

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    model = Products
    search_fields = ("code","name",) 
    
class StockTransactionlinesInline(admin.TabularInline):
    model = StockTransactionlines
    extra = 1
    raw_id_fields = ['product',]
    autocomplete_fields = ['product'] 
      
    
@admin.register(StockTransactions)
class StockTransactionsAdmin(admin.ModelAdmin):
    inlines = [StockTransactionlinesInline]
    

admin.site_header = "Inventory Management"


