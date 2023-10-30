"""
symbol = "MSFT"
df = yf.Ticker(symbol)
df = msft.history(period="max)
df["Returns"] = df["Closer"].pct_change()
"""
