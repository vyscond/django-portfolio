from __future__ import unicode_literals
from django.db import models


class Broker(models.Model):
    name = models.CharField(max_length=256)
    buy_fee = models.DecimalField(max_digits=8, decimal_places=2)
    sell_fee = models.DecimalField(max_digits=8, decimal_places=2)


class StockExchange(models.Model):
    name = models.CharField(max_length=256)
    emoluments_fee = models.FloatField()
    liquidation_fee = models.FloatField()
    registry_fee = models.FloatField()

    @property
    def total(self):
        return self.emoluments_fee + self.liquidation_fee + self.registry_fee

    def __str__(self):
        return '{} ({})'.format(self.name, self.total)


class Stock(models.Model):
    symbol = models.CharField(max_length=256)

    def __str__(self):
        return self.symbol


class Sell(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    stock = models.ForeignKey(Stock)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()


class Buy(models.Model):
    date = models.DateTimeField()
    stock = models.ForeignKey(Stock)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField()
