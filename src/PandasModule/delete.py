import pandas as pd
import numpy as np

serie = pd.Series(np.arange(4), index=['a', 'b', 'c', 'd'])
print(serie)
deleted = serie.drop('c')
print(deleted)

data = np.arange(9).reshape(3,3)
print(data)

lista_indices = ['a', 'b', 'c']
lista_columnas = ['c1', 'c2', 'c3']
dataframe = pd.DataFrame(data, index=lista_indices, columns=lista_columnas)
print(dataframe)

filtered = dataframe.drop('b')
print(filtered)