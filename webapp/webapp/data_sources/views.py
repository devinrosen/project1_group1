import logging

from rest_framework import generics, status
from rest_framework.response import Response

from .import models
from .import serializers
from .constants import DATA_SOURCES
from .utils import DATA_SOURCE_FUNCTION

logging.basicConfig()
log = logging.getLogger(__name__)


class DataSources(generics.ListAPIView):
    """
    The data sources app is driven from a defined collection of sources
    that the app knows how to interact with
    """
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        return Response(DATA_SOURCES, status.HTTP_200_OK)


class DataSource(generics.ListAPIView):
    """
    The data sources app is driven from a defined collection of sources
    that the app knows how to interact with
    """
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.CompanyTickerSerializer
    queryset = models.Company.objects

    def get(self, request, source):
        if source not in DATA_SOURCES:
            return Response({"Unsupported data source": source}, status.HTTP_400_BAD_REQUEST) # NOQA
        return super().get(request, source)


class DataSeries(generics.RetrieveAPIView):
    """
    The data sources app is driven from a defined collection of sources
    that the app knows how to interact with
    """
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.CompanySerializer
    queryset = models.Company.objects

    def get_object(self):
        source = self.kwargs["source"]
        series = self.kwargs["series"]

        try:
            return self.queryset.get(symbol=series)
        except Exception:
            return DATA_SOURCE_FUNCTION[source](series)

    def get(self, request, source, series):
        if source not in DATA_SOURCE_FUNCTION:
            return Response({"Unsupported data source": source}, status.HTTP_400_BAD_REQUEST) # NOQA
        return super().get(request, source, series)
