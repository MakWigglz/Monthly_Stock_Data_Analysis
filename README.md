# Monthly_Stock_Data_Analysis
Excellent question, Mak. Here's **exactly how to get 15 years of monthly average stock prices** in dollars for **3 companies in the same sector** (e.g., banks) using `yfinance` and Python.

---

## ✅ Step-by-Step Plan

### ✅ 1. **Pick 3 Bank Stocks**

Examples of U.S. bank stocks:

* **JPM** – JPMorgan Chase
* **BAC** – Bank of America
* **WFC** – Wells Fargo
* Added Apple and British Petroluem stocks

### ✅ 2. **Install and Import Libraries**

```bash
pip install yfinance pandas
```

```python
import yfinance as yf
import pandas as pd
```

---

### ✅ 3. **Download Monthly Stock Data for 15 Years**

```python
# List of bank tickers
tickers = ['JPM', 'BAC', 'WFC']

# Create an empty DataFrame
monthly_data = pd.DataFrame()

# Download data for each ticker
for ticker in tickers:
    df = yf.download(ticker, start='2010-01-01', end='2025-01-01', interval='1mo')
    df['Ticker'] = ticker
    df['Date'] = df.index
    df = df[['Date', 'Close', 'Ticker']]
    monthly_data = pd.concat([monthly_data, df])
```

---

### ✅ 4. **Result: Monthly Average Closing Prices**

```python
# Pivot to get monthly average prices per stock
monthly_avg_prices = monthly_data.pivot(index='Date', columns='Ticker', values='Close')

# Show head
print(monthly_avg_prices.head())
```

This will give you a DataFrame like:

| Date       | BAC   | JPM   | WFC   |
| ---------- | ----- | ----- | ----- |
| 2010-01-31 | 15.23 | 40.22 | 27.55 |
| 2010-02-28 | 15.78 | 41.01 | 28.12 |
| ...        | ...   | ...   | ...   |

Each value is the **closing price** on the last day of the month (typical for financial data), which you can treat as the **monthly price**.

---

### ✅ 5. (Optional) Save to CSV

```python
monthly_avg_prices.to_csv("bank_stocks_15yrs_monthly.csv")
```

---

### ✅ 6. (Optional) Plot It

```python
monthly_avg_prices.plot(title="Monthly Closing Prices (2010–2025)", figsize=(12,6))
```

---

## ✅ Summary

* You downloaded **15 years of monthly data** using `interval='1mo'`
* Used `.pivot()` to create a **multi-company table**
* You now have a **clean, long-term dataset** perfect for:

  * Moving averages
  * Levene’s and t-tests between banks
  * Sector performance comparisons

---

Would you like help applying Shapiro or Levene on these monthly prices next?
