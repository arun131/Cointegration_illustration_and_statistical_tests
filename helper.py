import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def trim_and_split_data(data, start_date, end_date):

    # Split the data into train and test sets
    train_data = data[start_date:end_date]
    test_data = data[end_date:datetime.now().date()]
    
    return train_data, test_data

def plot_pair(pair_a_prices, pair_b_prices, pair_a_name = "Asset_A", pair_b_name = "Asset_B"):
    try:
      index_a = pair_a_prices.index
      index_b = pair_b_prices.index
      values_a = pair_a_prices.values
      values_b = pair_b_prices.values
    except Exception as e:
      index_a = np.arange(len(pair_a_prices))
      index_b = np.arange(len(pair_b_prices))
      values_a = pair_a_prices 
      values_b = pair_b_prices 

    # plot the figure
    fig, ax1 = plt.subplots()
    ax1.set_xlabel('Date')
    ax1.set_ylabel(pair_a_name)
    ax1.plot(index_a, values_a, color = 'k')


    ax2 = ax1.twinx()  
    ax2.set_ylabel(pair_b_name)  
    ax2.plot(index_b, values_b, color = 'r')

    fig.tight_layout()  
    plt.show()