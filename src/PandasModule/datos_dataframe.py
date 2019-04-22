import pandas as pd
import numpy as np

lista_valores = np.arange(25).reshape(5,5)
lista_indices = ['i1','i2','i3','i4','i5']
lista_columnas = ['c1', 'c2', 'c3', 'c4', 'c5']
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)
print(dataframe)
getColumn  = dataframe['c2']['i2']
print(getColumn) # 6
