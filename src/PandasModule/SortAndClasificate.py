import pandas as pd
import numpy as np

lista_valores = range(4)
list_indices = list('CABD')
serie = pd.Series(lista_valores, index=list_indices)
sorted_index = serie.sort_index()
print(sorted_index)
sorted_value = serie.sort_values()
print(sorted_value)

list_rang = serie.rank()
print(list_rang)

serie2 = pd.Series(np.random.rand(10))
print(serie2)
list_rang2 = serie2.rank()
print(list_rang2)