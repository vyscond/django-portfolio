from django.contrib import admin
from portfolio.models import Broker
from portfolio.models import StockExchange
from portfolio.models import Stock


class BrokerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'buy_fee',
        'sell_fee',)


class StockExchangeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'emoluments_fee',
        'liquidation_fee',
        'registry_fee',
        'total',)


class StockAdmin(admin.ModelAdmin):
    list_display = ('symbol',)


admin.site.register(Broker, BrokerAdmin)
admin.site.register(StockExchange, StockExchangeAdmin)
admin.site.register(Stock, StockAdmin)
