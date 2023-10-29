import logging

import yfinance as yp

from .models import Series

logging.basicConfig()
log = logging.getLogger(__name__)


def update_history(symbol, period):
    ticker = yp.Ticker(symbol)
    history = ticker.history(period=period)
    history["Returns"] = history["Close"].pct_change()
    # Need to fill the empty return cell with zero; JSON does not support NaN
    history["Returns"] = history["Returns"].fillna(0)
    # Might have to compare performance of individual saves vs BATCH
    # https://docs.datastax.com/en/cql-oss/3.3/cql/cql_using/useBatchGoodExample.html
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
            daily_returns=row.loc["Returns"],
        )
        series_item.save()
