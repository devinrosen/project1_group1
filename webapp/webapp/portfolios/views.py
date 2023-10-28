import logging

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
