import pandas as pd
import numpy as np

list_value = ['1','2', np.nan, '4']
print(list_value)

serie = pd.Series(list_value, index=list('abcd'))
print(serie)

checker = serie.isnull()
print(checker)

delete_null = serie.dropna()
print(delete_null)

list_value = [[1,2,3], [4,np.nan, 5], [6,7, np.nan]]
print(list_value)

list_index = list('123')
list_columns = list('abc')

dataframe = pd.DataFrame(list_value, index=list_index, columns=list_columns)
print(dataframe)

check_null = dataframe.isnull()
print(check_null)

drop_null = dataframe.dropna()
print(drop_null)