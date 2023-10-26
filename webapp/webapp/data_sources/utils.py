import logging
import yfinance as yf

from rest_framework.exceptions import NotFound

from . import serializers

logging.basicConfig()
log = logging.getLogger(__name__)


def yahoo(series):
    try:
        series_data = yf.Ticker(series)
    except Exception:
        raise NotFound(detail=f"Invalid stock {series}")

    serializer = serializers.CompanySerializer(data=series_data.info)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return series_data.info


DATA_SOURCE_FUNCTION = {
    "yahoo": yahoo,
}