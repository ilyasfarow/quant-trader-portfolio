import numpy as np
import matplotlib.pyplot as plt

def evaluate(df):

    
    # Strategy returns
    df["Strategy_Return"] = df["Position"] * df["Return"]

    df = df.dropna()

    # Market stats
    mean_return = df["Return"].mean()
    volatility = df["Return"].std()

    annual_return = mean_return * 252
    annual_volatility = volatility * np.sqrt(252)

    risk_free_rate = 0.03
    sharpe = (annual_return - risk_free_rate) / annual_volatility

    # Strategy stats
    strategy_mean = df["Strategy_Return"].mean()
    strategy_vol = df["Strategy_Return"].std()

    strategy_annual_return = strategy_mean * 252
    strategy_annual_vol = strategy_vol * np.sqrt(252)

    strategy_sharpe = strategy_annual_return / strategy_annual_vol

    # Cumulative returns
    df["Cumulative_Market_Return"] = (1 + df["Return"]).cumprod()
    df["Cumulative_Strategy_Return"] = (1 + df["Strategy_Return"]).cumprod()

    # Plot equity curve
    plt.figure(figsize=(10,5))
    plt.plot(df["Cumulative_Market_Return"], label="Buy & Hold")
    plt.plot(df["Cumulative_Strategy_Return"], label="Strategy")
    plt.legend()
    plt.title("Strategy vs Market Performance")
    plt.show()

    # Drawdown
    df["Market_Peak"] = df["Cumulative_Market_Return"].cummax()
    df["Strategy_Peak"] = df["Cumulative_Strategy_Return"].cummax()

    df["Market_Drawdown"] = df["Cumulative_Market_Return"] / df["Market_Peak"] - 1
    df["Strategy_Drawdown"] = df["Cumulative_Strategy_Return"] / df["Strategy_Peak"] - 1
    
    
    Market_Drawdown =df["Market_Drawdown"].min()
    Strategy_Drawdown=df["Strategy_Drawdown"].min()

    print("Max Market Drawdown:", df["Market_Drawdown"].min())
    print("Max Strategy Drawdown:", df["Strategy_Drawdown"].min())

    # Plot drawdown
    plt.figure(figsize=(10,5))
    plt.plot(df["Market_Drawdown"], label="Market")
    plt.plot(df["Strategy_Drawdown"], label="Strategy")
    plt.legend()
    plt.title("Drawdown Comparison")
    plt.show(block=True)
    # added to stop code from running in a loop

    # Final report
    print("\n--- MARKET PERFORMANCE ---")
    print("Market annual return:", annual_return)
    print("Market annual volatility:", annual_volatility)
    print("Market Sharpe:", sharpe)

    print("\n--- STRATEGY PERFORMANCE ---")
    print("Strategy annual return:", strategy_annual_return)
    print("Strategy annual volatility:", strategy_annual_vol)
    print("Strategy Sharpe:", strategy_sharpe)
    return annual_return,annual_volatility,sharpe,strategy_annual_return,strategy_annual_vol,strategy_sharpe,Market_Drawdown,Strategy_Drawdown