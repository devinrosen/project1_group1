import logging

import yfinance as yp

from .models import Series

logging.basicConfig()
log = logging.getLogger(__name__)


def update_history(symbol):
    ticker = yp.Ticker(symbol)
    history = ticker.history()
    for index, row in history.iterrows():
        series_item = Series(
            date=index.date(),
            symbol=symbol,
            close=row.loc["Close"],
            open=row.loc["Open"],
            high=row.loc["High"],
            low=row.loc["Low"],
            volume=row.loc["Volume"],
            dividends=row.loc["Dividends"],
            stock_splits=row.loc["Stock Splits"],
        )
        series_item.save()
