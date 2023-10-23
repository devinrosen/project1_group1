from rest_framework import generics, status
from rest_framework.response import Response

from .constants import DATA_SOURCES
from .utils import DATA_SOURCE_FUNCTION


class DataSources(generics.ListAPIView):
    """
    The data sources app is driven from a defined collection of sources
    that the app knows how to interact with
    """
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        return Response(DATA_SOURCES, status.HTTP_200_OK)


class DataSource(generics.RetrieveAPIView):
    """
    The data sources app is driven from a defined collection of sources
    that the app knows how to interact with
    """
    permission_classes = []
    authentication_classes = []

    def get(self, request, source):
        if source not in DATA_SOURCES:
            return Response({"Unsupported data source": source}, status.HTTP_400_BAD_REQUEST) # NOQA
        return Response(DATA_SOURCES[source], status.HTTP_200_OK)


class DataSeries(generics.RetrieveAPIView):
    """
    The data sources app is driven from a defined collection of sources
    that the app knows how to interact with
    """
    permission_classes = []
    authentication_classes = []

    def get(self, request, source, series):
        if source not in DATA_SOURCE_FUNCTION:
            return Response({"Unsupported data source": source}, status.HTTP_400_BAD_REQUEST) # NOQA
        response = DATA_SOURCE_FUNCTION[source](series)
        return Response(response, status.HTTP_200_OK)