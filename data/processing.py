import pandas as pd
import numpy as np

def datahandling():

    filename = input("Enter your file name: ")
    data = pd.read_excel(f"data/{filename}")

    prices = data['Close']

    log_rets = np.log(prices/prices.shift(1)).dropna()

    S0 = prices.iloc[-1]
    std = log_rets.std()

    return S0, std

if __name__ == "__main__":
    datahandling()

