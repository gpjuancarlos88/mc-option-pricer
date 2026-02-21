from models import simulate_gbm_terminal
from analytics import black_scholes_merton_call
from pricer import mc_pricer
from data.processing import datahandling
import numpy as np

def main():

    S0, sigma = datahandling()
    sigma = sigma * np.sqrt(252)
    r = 0.05
    T = 1.0
    N = 1000000
    K = 110

    print("GBM Simulation: ")
    ST = simulate_gbm_terminal(S0, r, sigma, T, N, seed=42)
    print("First 5 simulated prices:", ST[:5])
    print("Mean:", ST.mean())

    print("MC Prices resluts:")
    mc_price, se, CI_D, CI_U = mc_pricer(ST,K,r,T)
    print("The value of the call option is: " + str(mc_price))

    BSM_price = black_scholes_merton_call(S0,K,sigma,T,r)
    print("BSM PRICE: " + str(BSM_price))

    print(f'the standard error of the simulation is {se}')
    print(f'the Confidence interval of te simulation is: Lower Bound:{CI_D}, Mean: {mc_price}, Upper Bound: {CI_U}')


if __name__ == "__main__":
    main()
