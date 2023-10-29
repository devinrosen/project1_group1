import logging

from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .import models
from .import serializers
from .utils import update_history

logging.basicConfig()
log = logging.getLogger(__name__)


class Series(generics.ListAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.SeriesSerializer
    queryset = models.Series.objects

    def get_queryset(self):
        symbol = self.kwargs.get("series")
        if not symbol:
            raise NotFound("Missing Symbol")
        return self.queryset.filter(symbol=symbol)


class UpdateSeries(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = serializers.UpdateSeriesSerializer
    queryset = models.Series.objects

    def update(self, request, *args, **kwargs):
        series = kwargs.get("series")
        period = request.data.get("period")
        update_history(series, period)
        return Response({"series": series}, status.HTTP_201_CREATED)
