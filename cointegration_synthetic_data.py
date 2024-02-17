import numpy as np
import matplotlib.pyplot as plt

def simple_method(plot = False):
  # Method 1: simple method to create a cointegrated pair
  n = 2000 # number of random values
  start_value = 200
  stand_dev = 2


  # generate stock prices
  # assuming geometric brownian motion  
  price_changes_1 = stand_dev * np.random.randn(n)
  stock_1 = start_value + np.cumsum(price_changes_1)

  # simple cointegrated 
  price_changes_2 = 2 * stand_dev * np.random.randn(n)
  stock_2 =  stock_1 * 2 + price_changes_2 

  if plot:
      # plot the prices
      plt.plot(stock_1)
      plt.plot(stock_2)

  return stock_1, stock_2

def adapted_method(plot = False):
  # Method 2: Adapted from A drunk and her dog method
  # https://www.researchgate.net/publication/254330798_A_Drunk_and_Her_Dog_An_Illustration_of_Cointegration_and_Error_Correction

  def make_cointegrated_pair(num_samples,start_values=[0,0],sigma=[1,1],coint_factor=[0.1,0.1]):
      N = num_samples 
      T0 = start_values
      c = coint_factor

      X = [0]
      Y = [0]
      for i in range(N):
          rx = np.random.randn()*sigma[0] - c[0]*(X[-1] - Y[-1])
          ry = np.random.randn()*sigma[1] + c[1]*(X[-1] - Y[-1])
          X.append(X[-1]+rx)
          Y.append(Y[-1]+ry)
      return np.array(X)+T0[0], np.array(Y)+T0[1]

  stock_1, stock_2 = make_cointegrated_pair(num_samples=2000, start_values= [100, 100], sigma = [0.01, 0.01], coint_factor=[0.1, 0.1])
  
  if plot:
    # plot the prices
    plt.plot(stock_1)
    plt.plot(stock_2)

  return stock_1, stock_2


def not_cointegrated(plot = False):
  # Not cointegrated pairs
  n = 2000 # number of random values
  start_value_1 = 200
  stand_dev_1 = 2

  start_value_2 = 250
  stand_dev_2 = 5

  # generate stock prices
  # assuming geometric brownian motion  
  price_changes_1 = stand_dev_1 * np.random.randn(n)
  stock_1 = start_value_1 + np.cumsum(price_changes_1)

  price_changes_2 = stand_dev_2 * np.random.randn(n)
  stock_2 = start_value_2 + np.cumsum(price_changes_2)

  return stock_1, stock_2

