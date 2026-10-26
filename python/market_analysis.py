import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

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

# NVIDIA market analysis

nvidia = yf.download(
  tickers="NVDA",
  start="2025-01-01",
  end="2026-01-01",
  auto_adjust=True
)

nvidia_prices = nvidia["Close"]["NVDA"]
nvidia_returns = nvidia_prices.pct_change().dropna()

def calculate_statistics(returns):
  average_return = np.mean(returns)
  daily_volatility = np.std(returns)
  annual_volatility = daily_volatility*np.sqrt(252)
  return average_return, daily_volatility, annual_volatility

nvidia_average_return, nvidia_daily_volatility, nvidia_annual_volatility = calculate_statistics(nvidia_returns)

print(f"NVIDIA Avergae Daily Return: {nvidia_average_return:.2%}")
print(f"NVIDIA Daily Volatility: {nvidia_daily_volatility:.2%}")
print(f"NVIDIA Annual Volatility: {nvidia_annual_volatility:.2%}")

apple_avergare_return, apple_daily_volatility, apple_annual_volatility = calculate_statistics(apple_returns)

print(f"Average Daily Return: {apple_average_return:.2%}")
print(f"Daily Volatility: {apple_daily_volatility:.2%}")
print(f"Annual Volatility: {apple_annual_volatility:.2%}")

# S&P 500 market analysis
sp500 = yf.download(
  tickers="^GSPC",
  start="2025-01-01",
  end="2026-01-01",
  auto_adjust=True
)

sp500_prices = sp500["Close"]["^GSPC"]
sp500_returns = sp500_prices.pct_change().dropna()

sp500_average_return, sp500_daily_volatility, sp500_annual_volatility = calculate_statistics(sp500_returns)

print(f"S&P 500 Average Daily Return: {sp500_average_return:.2%}")
print(f"S&P 500 Daily Volatility: {sp500_daily_volatility:.2%}")
print(f"S&P 500 Annual Volatility: {sp500_annual_volatility:.2%}")

returns_data = {
  "Apple": apple_returns,
  "Nvidia": nvidia_returns,
  "S&P 500": sp500_returns
}
returns_df = pd.DataFrame(returns_data)
print(returns_df)

correlation_matrix = returns_df.corr()
print(correlation_matrix)

apple_covariance = returns_df["Apple"].cov(returns_df["S&P 500"])
market_variance = returns_df["S&P 500"].var()
apple_beta = apple_covariance/market_variance
print(f"Apple Beta: {apple_beta:.2f}")

nvidia_covariance = returns_df["Nvidia"].cov(returns_df["S&P 500"])
nvidia_beta = nvidia_covariance/market_variance
print(f"Nvidia Beta: {nvidia_beta:.2f}")

# CAPM expected return analysis
risk_free_rate = 0.04
expected_market_return = 0.10
apple_expected_return = risk_free_rate + apple_beta * (expected_market_return - risk_free_rate)
nvidia_expected_return = risk_free_rate + nvidia_beta * (expected_market_return - risk_free_rate)
    
print(f"Apple CAPM Expected Return: {apple_expected_return:.2%}")
print(f"Nvidia CAPM Expected Return: {nvidia_expected_return:.2%}")

# Visualize cumulative returns

cumulative_returns = (1 + returns_df).cumprod()
cumulative_returns.plot(figsize=(10,6))

plt.title("Cumulative Returns: Apple vs Nvidia vs S&P 500")
plt.xlabel("Date")
plt.ylabel("Growth of $1 Investment")
plt.grid(True)
plt.show()

# Risk vs return visualization

assets = ["Apple", "Nvidia", "S&P 500"] 

annual_returns = [
  apple_average_return * 252,
  nvidia_average_return * 252,
  sp500_average_return * 252
]

annual_volatilities = [
  apple_annual_volatility,
  nvidia_annual_volatility,
  sp500_annual_volatility
]

plt.figure(figsize=(8, 6))
plt.scatter(annual_volatilities, annual_returns)

for i, asset in enumerate(assets):
    plt.annotate(asset, (annual_volatilities[i], annual_returns[i]))

plt.title("Risk vs Return")
plt.xlabel("Annualized Volatility")
plt.ylabel("Annualized Average Return")
plt.grid(True)
plt.show()

             
