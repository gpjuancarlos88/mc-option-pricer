import yfinance as yf
import pandas as pd

def datapipeline():
        
    ticker = input("Enter ticker symbol: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    data = yf.download(ticker, start=start_date, end=end_date, interval="1d")

    # Flatten MultiIndex columns if present
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]

    filename = f"{ticker}_DATA.xlsx"
    data.to_excel(filename, index=True)

    return data

if __name__ == "__main__":
    datapipeline()


