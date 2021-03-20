from django.contrib import admin
from stockreceipts.models import Products
from stocktransactions.models import StockTransactions , StockTransactionlines

class StockTransactionlinesInline(admin.TabularInline):
    model = StockTransactionlines

class StockTransactionlinese(admin.ModelAdmin):
    list_filter=('datenew')
    model = StockTransactionlines

@admin.register(StockTransactions)
class StockTransactionsAdmin(admin.ModelAdmin):
    inlines = [StockTransactionlinesInline]

admin.site_header = "Inventory Management"
admin.site.register(Products)

