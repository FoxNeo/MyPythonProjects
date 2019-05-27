import pandas as pd
import numpy as np

list_values = np.random.rand(6)
list_index = [[1,1,1,2,2,2], ['a', 'b', 'c', 'a', 'b', 'c']]
series = pd.Series(list_values, index=list_index)
first = series[1]

dataframe = series.unstack()
print(dataframe)

list_values = np.arange(16).reshape(4,4)
print(list_values)

list_index = list('1234')
print(list_index)

list_columns = list('abcd')
dataframe2 = pd.DataFrame(list_values, index=list_index, columns=list_columns)
print(dataframe2)

serie2 = dataframe2.stack()
print(serie2)