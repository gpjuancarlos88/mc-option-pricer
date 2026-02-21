import numpy as np
from scipy.stats import norm

def simulate_gbm_terminal(S0, r, sigma, T, N, seed=None):

    rng = np.random.default_rng(seed)
    Z = rng.standard_normal(N)
    drift = (r - 0.5 * sigma**2) * T
    diffusion = sigma * np.sqrt(T) * Z

    S_T = S0 * np.exp(drift + diffusion)

    return S_T