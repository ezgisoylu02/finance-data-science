# Finance Data Science Project

A Python project exploring financial markets through statistics, data analysis, and financial models.

This project is part of my learning journey combining finance, economics, statistics, and data science. Rather than only using pre-calculated financial metrics, I calculate and interpret them directly from real market data.

# Project Overview

The analysis compares:

- Apple (AAPL)
- NVIDIA (NVDA)
- S&P 500 (^GSPC) as the market benchmark

Using historical market data, the project analyzes returns, volatility, correlations, beta, CAPM expected returns, and cumulative investment growth.

# What the Project Calculates

### Daily Returns

Daily returns are calculated from consecutive adjusted stock prices:

Return = (New Price - Previous Price) / Previous Price

These returns form the basis of the rest of the analysis.

### Volatility

I calculate daily volatility using the standard deviation of daily returns.

Annualized volatility is estimated using:

Annual Volatility = Daily Volatility × √252

where 252 represents the approximate number of trading days in a year.

### Correlation

A correlation matrix compares how the daily returns of Apple, NVIDIA, and the S&P 500 move relative to each other.

In the analyzed sample:

- Apple and S&P 500 correlation ≈ 0.75
- NVIDIA and S&P 500 correlation ≈ 0.74
- Apple and NVIDIA correlation ≈ 0.44

This shows that both stocks had a relatively strong positive relationship with the broader market during the period, while their relationship with each other was weaker.

### Beta

Instead of retrieving beta from a financial website, I calculate it directly from market returns:

Beta = Covariance(Stock Return, Market Return) / Variance(Market Return)

Results:

- Apple Beta ≈ 1.30
- NVIDIA Beta ≈ 1.96

Both stocks had beta values above 1 in this sample, meaning their returns tended to be more sensitive to market movements than the S&P 500 benchmark.

NVIDIA's higher beta indicates substantially greater market sensitivity.

### CAPM

I use the Capital Asset Pricing Model:

Expected Return = Risk-Free Rate + Beta × (Expected Market Return - Risk-Free Rate)

Using an assumed:

- Risk-free rate = 4%
- Expected market return = 10%

the model produces:

- Apple CAPM Expected Return ≈ 11.79%
- NVIDIA CAPM Expected Return ≈ 15.77%

These are model-based expected returns rather than predictions of what the stocks will actually return.

## Visualizations

### Cumulative Returns

The project compares how a hypothetical $1 investment would have grown over the sample period.

The chart demonstrates that NVIDIA experienced much larger fluctuations but also achieved substantially greater cumulative growth during the analyzed period.

### Risk vs Return

The second visualization compares annualized volatility with annualized arithmetic average daily returns.

The sample illustrates an important point: higher volatility does not automatically produce higher returns.

Apple experienced considerably higher volatility than the S&P 500 while having a similar annualized arithmetic average return in this sample. NVIDIA, meanwhile, combined much higher volatility with a much higher arithmetic average return.

## Key Takeaways

This project helped me connect financial theory with actual market data.

I learned how to:

- retrieve and organize financial data with Python
- calculate and analyze daily returns
- measure volatility
- interpret correlations between financial assets
- calculate covariance and beta
- apply CAPM
- distinguish systematic market sensitivity from total volatility
- visualize cumulative investment performance
- compare risk and return quantitatively

One of the most important lessons from the analysis is that risk cannot be described by a single number. Volatility, correlation, and beta measure different aspects of financial risk.

The results are also sample-dependent. Historical relationships such as beta, correlation, volatility, and returns can change when a different time period or market benchmark is used.

## Tools

- Python
- pandas
- NumPy
- yfinance
- Matplotlib
- Google Colab
- GitHub

## Next Steps

This project provides a foundation for more advanced work in financial data science. Future extensions could include:

- regression-based beta estimation
- longer historical periods
- comparison across different market regimes
- additional assets and benchmarks
- econometric analysis
- portfolio optimization
- time-series analysis
- machine learning

## Disclaimer

This project is for educational and analytical purposes only and should not be considered financial advice.
