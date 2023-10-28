import yfinance as yp

from .models import Series

def save_history(symbol):
    ticker = yp.Ticker(symbol)
    history = ticker.history()
    for index, row in history.iterrows():
       log.critical(f"{index} {row.loc['Close']}")
       series_item = Series(
           
       )
       series_item.save()
