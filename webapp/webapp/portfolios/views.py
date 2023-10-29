import logging

import pandas as pd

from bokeh.plotting import figure
from bokeh.embed import components
from django.shortcuts import render
from rest_framework import generics

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

        return render(request, 'base.html', context=kwargs)
