import pandas as pd
import numpy as np

def datahandling():

    data = pd.read_excel(input("Enter your file name"))

    prices = data['Close']

    log_rets = np.log(prices/prices.shift(1)).dropna()

    S0 = prices.iloc[-1]
    std = log_rets.std()

    return S0, std

datahandling()

