import numpy as np
from models import simulate_gbm_terminal

def mc_pricer(ST, K, r, T):

    payoff = np.maximum(ST-K,0)
    discounted_payoff = np.exp(-r*T) * payoff
    price = discounted_payoff.mean()
    standard_error = discounted_payoff.std(ddof = 1) / np.sqrt(len(discounted_payoff))
    CI_U = price + 1.96*standard_error
    CI_D = price - 1.96*standard_error


    return price, standard_error, CI_D, CI_U