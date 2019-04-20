import pandas as pd

lista_valores = [1,2,3]
lista_indices = ['a', 'b', 'c']
serie = pd.Series(lista_valores, index=lista_indices)
print(serie)

lista_notas = [[6,7,8],[8,9,5],[6,9,7]]
lista_indices2 = ['Matematicas', 'historia', 'fisica']
lista_nombres = ['Antonio', 'Maria', 'Pedro']

dataframe = pd.DataFrame(lista_notas, index=lista_indices2, columns=lista_nombres)
print(dataframe)
print(dataframe.index)