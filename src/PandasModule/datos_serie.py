import pandas as pd
import numpy as np

lista_valores = np.arange(3)
print(lista_valores)

lista_indices = ['i1', 'i2', 'i3']
serie = pd.Series(lista_valores, index=lista_indices)
print(serie)

print(serie['i2'])
print(serie[0:3]) # initial end
print(serie['i1':'i2'])


