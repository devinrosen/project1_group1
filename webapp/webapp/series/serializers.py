import logging

from rest_framework import serializers

logging.basicConfig()
log = logging.getLogger(__name__)


class UpdateSeriesSerializer(serializers.Serializer):
    pass


class SeriesSerializer(serializers.Serializer):
    date = serializers.CharField()
    open = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    close = serializers.FloatField()
    volume = serializers.FloatField()
    dividends = serializers.FloatField()
    stockSplits = serializers.FloatField(source="stock_splits")
