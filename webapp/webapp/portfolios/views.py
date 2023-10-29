import logging

import pandas as pd

from bokeh.plotting import figure
from bokeh.embed import components
from django.shortcuts import render
from rest_framework import generics

from series.models import Series

from .import models
from .import serializers

logging.basicConfig()
log = logging.getLogger(__name__)


class Portfolios(generics.ListCreateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.PortfolioSerializer
    queryset = models.Portfolio.objects


class Portfolio(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.PortfolioSerializer
    queryset = models.Portfolio.objects


class ExplorePortfolio(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.PortfolioSerializer
    queryset = models.Portfolio.objects

    def get(self, request, pk):
        # Get the portfolio
        portfolio = self.get_object()

        kwargs = {
            "portfolio": portfolio,
            "plots": {
                "distribution": {},
                "returns": {},
                "correlation": {},
            },
        }

        # Create the distribution script and div
        symbols = []
        weights = []
        for k, v in portfolio.holdings.items():
            symbols.append(k)
            weights.append(v)
        plot = figure(frame_width=400, frame_height=400, x_range=symbols)
        plot.vbar(x=symbols, top=weights, width=0.5)
        distribution_script, distribution_div = components(plot)
        kwargs["plots"]["distribution"]["script"] = distribution_script
        kwargs["plots"]["distribution"]["div"] = distribution_div
        # Create the distribution script and div

        # Create the data frame
        dfs = {}
        for symbol in symbols:
            date = []
            close = []
            returns = []
            try:
                series_data = Series.objects.filter(symbol=symbol).values_list(
                    "date",
                    "close",
                    "daily_returns"
                )
                for data in series_data:
                    date.append(data[0])
                    close.append(data[1])
                    returns.append(data[2])
                dfs[symbol] = pd.DataFrame(
                    {f"{symbol} close": close, f"{symbol} returns": returns},
                    index=date
                )
            except Exception:
                log.exception(f"Unable to get series data for {symbol}")

        portfolio_df = pd.concat(dfs.values(), axis=1, join="inner")
        log.exception(f"{portfolio_df.head()}")
        # Create the data frame

        return render(request, 'base.html', context=kwargs)
