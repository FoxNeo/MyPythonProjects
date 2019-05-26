import pandas as pd
import numpy as np

array = np.array([[1,8,3], [5,6,7]])

dataframe = pd.DataFrame(array, index=['a', 'b'], columns=list('123'))

sumaDtaframe = dataframe.sum()
print(sumaDtaframe)
sumaDtaframecolumn = dataframe.sum(axis=1)
print(sumaDtaframecolumn)

getDataframeMin = dataframe.min()
print(getDataframeMin)

getDataframeMax = dataframe.max()
print(getDataframeMax)

report = dataframe.describe()
print(report)