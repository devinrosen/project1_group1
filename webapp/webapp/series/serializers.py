import logging

from rest_framework import serializers

logging.basicConfig()
log = logging.getLogger(__name__)

PERIOD_CHOICES = {
    "1mo": "1mo",
    "max": "max",
}


class UpdateSeriesSerializer(serializers.Serializer):
    period = serializers.ChoiceField(choices=PERIOD_CHOICES)


class SeriesSerializer(serializers.Serializer):
    date = serializers.CharField()
    open = serializers.FloatField()
    high = serializers.FloatField()
    low = serializers.FloatField()
    close = serializers.FloatField()
    volume = serializers.FloatField()
    dividends = serializers.FloatField()
    stockSplits = serializers.FloatField(source="stock_splits")
    dailyReturns = serializers.FloatField(source="daily_returns")
