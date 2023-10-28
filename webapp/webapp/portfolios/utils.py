from data_sources.models import Company
from data_sources.utils import DATA_SOURCE_FUNCTION

def validate_symbol(symbol):
    source = "yahoo"
    try:
        return Company.objects.get(symbol=symbol)
    except Exception:
        return DATA_SOURCE_FUNCTION[source](symbol)
