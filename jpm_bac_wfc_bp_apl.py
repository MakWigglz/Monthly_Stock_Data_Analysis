import yfinance as yf
import pandas as pd
import sqlite3

tickers = ['JPM', 'BAC', 'WFC', 'AAPL', 'BP']
monthly_price_data = pd.DataFrame()
monthly_volume_data = pd.DataFrame()

for ticker in tickers:
    df = yf.download(ticker, start='2007-01-01', end='2025-01-01', interval='1mo')
    df['Ticker'] = ticker
    df['Date'] = df.index
    price_df = df[['Date', 'Close', 'Ticker']]
    monthly_price_data = pd.concat([monthly_price_data, price_df])
    volume_df = df[['Date', 'Volume', 'Ticker']]
    monthly_volume_data = pd.concat([monthly_volume_data, volume_df])

# Pivot prices
monthly_avg_prices = monthly_price_data.pivot(index='Date', columns='Ticker', values='Close')

# Pivot volume
monthly_total_volume = monthly_volume_data.pivot(index='Date', columns='Ticker', values='Volume')
print("Monthly Prices:")
print(monthly_avg_prices.head())

print("\nMonthly Total Volume Traded:")
print(monthly_total_volume.head())

# Optional: Save to CSV
monthly_avg_prices.to_csv("stocks_monthly_prices_2007_2025.csv")
monthly_total_volume.to_csv("stocks_monthly_volume_2007_2025.csv")

merged_df = df[["Date", "Ticker", "Close", "Volume"]]
all_data = pd.concat([all_data, merged_df])
conn = sqlite3.connect("stocks_monthly_price.db")
# save DF to SQL
all_data.to_sql('stock_monthly', conn, if_exists='replace', index=False)

# Commit and close
conn.commit()
conn.close()
