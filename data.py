#import yfinance as yf

#def get_data():
#    df = yf.download("NVDA", start="2015-01-01", end="2026-10-03")
#    df = df.sort_index()
#    return df

import yfinance as yf

def get_data(ticker):
    df = yf.download(ticker, start="2015-01-01", end="2026-10-03")
    return df.sort_index()