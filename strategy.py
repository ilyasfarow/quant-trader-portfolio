#def apply_strategy(df):
    # Average volatility threshold
   # avg_rolling_vol = df["Rolling Volatility (20d)"].mean()

    # Signal: low volatility
   ## df["Low_Volatility"] = (
    #    df["Rolling Volatility (20d)"] < avg_rolling_vol
   # ).astype(int)

    # Position (shift to avoid look-ahead bias)
    #df["Position"] = df["Low_Volatility"].shift(1)

    #return df



def apply_strategy(df):
    # Average volatility threshold
    avg_rolling_vol = df["Rolling Volatility (20d)"].mean()

    # Signal: low volatility
    df["Low_Volatility"] = (
        df["Rolling Volatility (20d)"] < avg_rolling_vol
    ).astype(int)

    # Position (shift to avoid look-ahead bias)
    df["Position"] = df["Low_Volatility"].shift(1)

    # Strategy returns
    df["Strategy_Return"] = df["Position"] * df["Return"]

    # Drop NaN values created by shift
    df = df.dropna()

    # Cumulative returns
    df["Cumulative_Market"] = (1 + df["Return"]).cumprod()
    df["Cumulative_Strategy"] = (1 + df["Strategy_Return"]).cumprod()

    return df