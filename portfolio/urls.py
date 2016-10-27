from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'stocks/', views.StockList.as_view(), name='stock-list'),
    url(r'transaction/buy', views.BuyCreate.as_view(), name='transaction-buy'),
]
