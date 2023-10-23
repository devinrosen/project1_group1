import yfinance as yf


def yahoo(series):
    series_data = yf.Ticker(series)
    return series_data.info

DATA_SOURCE_FUNCTION = {
    "yahoo": yahoo,
}