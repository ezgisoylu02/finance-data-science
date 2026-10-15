import numpy as np

# Python fundamentals practice
# Practicing dictionaries, functions, and conditional statements
# using simple financial examples.
stock_1 = {
  "company": "NovaTech",
  "ticker": "NOVA",
  "price": 270,
  "beta": 1.4
}

stock_2 = {
  "company": "Diyot",
  "ticker": "DIO",
  "price": 320,
  "beta": -0.3
}

def analyze_stock(stock):
  if stock["beta"] > 1:
    return("High market sesitivity")
  elif stock["beta"] < 1:
    return("Low market sensitivity")
  else: return("Market-level sensitivity")

  print(stock_1["ticker"], analyze_stock(stock_1))
  print(stock_2["ticker"], analyze_stock(stock_2))
  

# Return analysis
returns = np.array([1.5,-0.7,2.3,-1.1,0.9])
average_return = np.mean(returns)
print(average_return)

volatility = np.std(returns)
print(volatility)

def analyze_returns(returns):
  average_return = np.mean(returns)
  volatility = np.std(returns)
  return average_retun, volatility

avg, vol = analyze_returns(returns)
print("Average Return:", avg)
print("Volatility:", vol)

def classify_volatility(vol):
  if vol < 1:
    return("Low volatility")
  elif vol <= 2:
    return("Moderate volatility")
  else:
    return("High volatility")

risk_level = classify_volatility(vol)
print("Risk Level:", risk_level)
