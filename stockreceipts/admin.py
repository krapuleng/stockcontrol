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
    readonly_fields= ('get_transactions_total',)
    list_display = ("datenew",'person','get_transactions_total',)
    list_per_page = 25
    date_hierarchy = 'datenew'
    inlines = [StockTransactionlinesInline]

    
admin.site.site_header = "Stock Management"
admin.site.site_title = "Stock ManagementPortal"
admin.site.index_title = "Stock Management Portal"


