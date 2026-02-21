import numpy as np
from scipy.stats import norm

def black_scholes_merton_call(S0, K, std, T, r):

    d1 = ((np.log(S0/K) + (r + 0.5*std**2))*T)/(std*np.sqrt(T))
    d2 = d1 - std*np.sqrt(T)

    call_value = S0*norm.cdf(d1)-K*np.exp(-r*T)*norm.cdf(d2)


    return call_value