from hurst import compute_Hc
import numpy as np
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
import statsmodels.api as sm

def mean_reversion_test(spread):
  exponent = hurst_exponent_test(spread)
  eg_res = engle_granger_test(spread)

  return exponent < 0.5 and eg_res


def hurst_exponent_test(data):
    """
    Compute the Hurst exponent to assess mean reversion.
    
    Parameters:
    - data: 1D array-like, the time series data
    
    Returns:
    - hurst_exponent: float, the estimated Hurst exponent
    - h < 0.5 -- The time series is mean reverting
    - h = 0.5 -- The time series is a Geometric Brownian Motion
    - h > 0.5 -- The time series is trending
    """
    H, c, data_range = compute_Hc(data)
    return H

def ornstein_uhlenbeck_test(data):
    """
    Fit an Ornstein-Uhlenbeck process to the data and estimate mean reversion parameters.
    
    Parameters:
    - data: 1D array-like, the time series data
    
    Returns:
    - mean_reversion_speed: float, the estimated mean reversion speed
      - higher the  mean_reversion_speed, higher mean reverting strength it has
    - long_term_mean: float, the estimated long-term mean
      - lower the long_term_mean, higher mean reverting strength it has
    """
    delta_t = 1  # Time interval, assuming data is sampled at regular intervals
    theta = -np.log(abs(data.mean())) / delta_t
    mu = data.mean()
    return theta, mu

def engle_granger_test(residuals):
    """
    Perform the Engle-Granger two-step cointegration test.
    
    Parameters:
    - data1, data2: 1D array-like, the time series data for two assets
    
    Returns:
    - is_cointegrated: bool, True if the assets are cointegrated and mean reverting (i.e., mean-reverting), False otherwise
    """

    # Step 2: Test residuals for stationarity
    adf_result = adfuller(residuals)
    kpss_result = kpss(residuals)
    
    is_cointegrated = adf_result[1] < 0.05 and kpss_result[1] > 0.05
    return is_cointegrated

def mean_reverting_half_life(spread):
    """
    Calculate the half-life of mean reversion for a spread series.

    Parameters:
    - spread: array-like, the spread series for which to calculate the half-life of mean reversion

    Returns:
    - half_life: float, the estimated half-life of mean reversion

    This function calculates the half-life of mean reversion for a given spread series.
    The spread series is assumed to represent the difference between two time series that are expected to revert to a long-term mean.
    The half-life of mean reversion is estimated using linear regression on the spread series.

    The calculation involves the following steps:
    1. Calculate the lagged spread series.
    2. Compute the returns as the difference between the spread series and its lagged version.
    3. Add a constant term to the lagged spread series.
    4. Perform ordinary least squares (OLS) regression on the returns with the lagged spread series as the independent variable.
    5. Calculate the half-life of mean reversion as the negative natural logarithm of 2 divided by the coefficient of the lagged spread series in the regression.

    Note: This function assumes that the spread series contains at least two observations.

    Example:
    >>> spread = [0.1, 0.2, 0.3, 0.2, 0.1]
    >>> half_life = mean_reverting_half_life(spread)
    >>> print(half_life)
    """

    lag_spread = np.roll(spread, 1)
    returns = spread - lag_spread
    const = sm.add_constant(lag_spread)
    model = sm.OLS(returns[1:], const[1:])
    res = model.fit()
    half_life = -np.log(2) / res.params[1]
    return half_life