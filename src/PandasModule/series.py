import pandas as pd

serie1 = pd.Series([3,5,7])
print(serie1)

print(serie1[1])
asignaturas = ['Mate', 'history', 'physic', 'Literatur']
notas = [8,6,9,7]
serie_notas_anonymous = pd.Series(notas, index=asignaturas)
print(serie_notas_anonymous)
print(serie_notas_anonymous['history'])
result = serie_notas_anonymous.name = ('Notas de Anonymous')
print(result)

diccionario = serie_notas_anonymous.to_dict()
print(diccionario)

serie = pd.Series(diccionario)
print(serie)