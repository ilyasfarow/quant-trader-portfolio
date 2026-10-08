
def add_features(df):
    # Returns
    df["Return"] = df["Close"].pct_change()

    # Rolling volatility (20d)
    df["Rolling Volatility (20d)"] = df["Return"].rolling(20).std()
    # tlenght of tiime for data
    df["SMA_10"] = df["Close"].rolling(10).mean()
    df["SMA_50"] = df["Close"].rolling(50).mean()
    df = df.dropna()
    return df