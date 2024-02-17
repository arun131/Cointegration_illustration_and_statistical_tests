import numpy as np
from statsmodels.tsa.stattools import adfuller, coint
from statsmodels.tsa.vector_ar.vecm import coint_johansen
from scipy.stats import spearmanr, kendalltau, pointbiserialr, pearsonr
from scipy.spatial.distance import correlation
from helper import plot_pair

def correlation_tests(A, B):
    """
    Calculate various correlation coefficients between two time series.

    Args:
    - A (pd.Series or np.ndarray): First time series.
    - B (pd.Series or np.ndarray): Second time series.

    Returns:
    - Tuple of correlation coefficients: Pearson, Spearman, Kendall's Tau, Point Biserial, and Distance correlation.
    """

    # Pearson correlation coefficient
    pearson_corr, _ = pearsonr(A, B)  # Pearson correlation coefficient

    # Spearman rank correlation
    spearman_corr, _ = spearmanr(A, B)  # Spearman rank correlation

    # Kendall's Tau
    kendall_tau, _ = kendalltau(A, B)  # Kendall's Tau

    # Point Biserial Correlation
    point_biserial_corr, _ = pointbiserialr(A, B)  # Point Biserial Correlation

    # Distance Correlation
    dist_corr = correlation(A, B)  # Distance Correlation

    return pearson_corr, spearman_corr, kendall_tau, point_biserial_corr, dist_corr


def calculate_basic_statistics(A, B):
    # Mean
    mean_A = np.mean(A)
    mean_B = np.mean(B)
    
    # Standard deviation
    std_A = np.std(A)
    std_B = np.std(B)
    
    return mean_A, mean_B, std_A, std_B


def perform_cointegration_tests(A, B):
    """
    Perform multiple cointegration tests on two time series.

    Args:
    - A (pd.Series or np.ndarray): First time series.
    - B (pd.Series or np.ndarray): Second time series.

    Returns:
    - Tuple of test results: Results of Engle-Granger, Johansen, Phillips-Ouliaris, and ADF-GLS tests.
    """

    # Four tests to test co-integration each return different results

    # Engle-Granger Test
    eg_result = coint(A, B, trend='c')  # Result of Engle-Granger test

    # Johansen Test
    johansen_result = coint_johansen(np.vstack((A, B)).T, det_order=0, k_ar_diff=1)  # Result of Johansen test

    # Phillips-Ouliaris Test
    po_result = adfuller(A - B)  # Result of Phillips-Ouliaris test

    # ADF-GLS Test
    adf_gls_result = adfuller(A - B, autolag='AIC', regression='ct')  # Result of ADF-GLS test

    return eg_result, johansen_result, po_result, adf_gls_result


def determine_cointegration(A, B, if_plot=False):
    """
    Determine if two time series are cointegrated using multiple tests.

    Args:
    - A (pd.Series or np.ndarray): First time series.
    - B (pd.Series or np.ndarray): Second time series.
    - if_plot (bool): Whether to plot the time series if they are cointegrated.

    Returns:
    - Tuple of bools: Results of cointegration tests (Eg, Johansen, Phillips-Ouliaris, ADF-GLS).
    """

    # Perform cointegration tests
    eg_result, johansen_result, po_result, adf_gls_result = perform_cointegration_tests(A, B)

    # Check if each test indicates cointegration

    # Engle-Granger test
    eg_res = eg_result[1] < 0.05  # p-value < 0.05 indicates evidence of cointegration

    # Johansen test
    jon_res = johansen_result.lr1[0] > johansen_result.cvt[0, 1]  # Comparison of test statistic with critical value

    # Phillips-Ouliaris test
    po_res = po_result[1] < 0.05  # p-value < 0.05 indicates evidence of cointegration

    # ADF-GLS test
    adf_res = adf_gls_result[1] < 0.05  # p-value < 0.05 indicates evidence of cointegration

    # Plot the time series if they are cointegrated and if_plot is True
    if if_plot:
        plot_pair(A, B)

    return eg_res, jon_res, po_res, adf_res
