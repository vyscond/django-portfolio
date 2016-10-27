from django.views.generic import ListView
from django.views.generic import CreateView
from portfolio.models import Stock
from portfolio.models import Buy


class StockList(ListView):
    model = Stock
    context_object_name = 'stocks'
    template_name = 'portfolio/stocks/list.html'


class BuyCreate(CreateView):
    model = Buy
    context_object_name = 'buy'
    template_name = 'portfolio/stocks/buy.html'
    fields = (
        'date',
        'stock',
        'price',
        'quantity',)

    def get_initial(self):
        initial = super(BuyCreate, self).get_initial()
        if self.request.GET.get('symbol', None):
            initial['stock'] = Stock.objects.get(
                symbol=self.request.GET.get('symbol'))
        return initial

