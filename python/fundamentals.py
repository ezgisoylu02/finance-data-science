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
  
  
