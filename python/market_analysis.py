import numpy as np
import pandas as pd
import yfinance as yf
# Download Apple market data
apple = yf.download(
  tickers="AAPL",
  start="2025-01-01",
  end="2026-01-01",
  auto_adjust=True
)

# Select Apple closing prices
apple_prices = apple["Close"]["AAPL"]
apple_returns = apple_prices.pct_change().dropna()
# Calculate return and volatility
apple_average_return = np.mean(apple_returns)
apple_daily_volatility = np.std(apple_returns)
apple_annual_volatility = apple_daily_volatility*np.sqrt(252)

print(f"Average Daily Return: {apple_average_return:.2%}")
print(f"Daily Volatility: {apple_daily_volatility:.2%}")
print(f"Annual Volatility: {apple_annual_volatility:.2%}")
