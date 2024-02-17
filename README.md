In this repository, I am conducting cointegration analysis in finance using Python. Cointegration analysis is a statistical technique used to determine whether two or more time series are "cointegrated," meaning they share a long-term relationship despite potentially exhibiting short-term fluctuations.
https://en.wikipedia.org/wiki/Cointegration

Here's a breakdown of the files in this repository:

**Cointegration_illustration_and_tests.ipynb:**

This Jupyter notebook serves as the main demonstration of cointegration analysis methods.
I generate random pairs of time series data, some with cointegration and others without.
I plot the data and visualize potential cointegration. Next, I perform four of the below cointegration tests on the data pairs to determine whether they exhibit cointegration or not.
- Engle-Granger test - https://www.statisticshowto.com/engle-granger-test/
- Johansen test - https://en.wikipedia.org/wiki/Johansen_test
- Phillips-Ouliaris test - http://math.furman.edu/~dcs/courses/math47/R/library/tseries/html/po.test.html
- ADF-GLS test - https://en.wikipedia.org/wiki/ADF-GLS_test

Finally, the results are presented with a summary.

**cointegration_synthetic_data.py:**

This Python script contains code for generating synthetic data for cointegration analysis.


**cointegration_tests.py:**

This Python script contains helper functions and implementations of cointegration tests.

**helper.py:**
This Python script contains additional helper functions for plotting and data manipulation.
