import pandas as pd
import webbrowser
website = 'https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA'
webbrowser.open(website)
dataframe_nba = pd.read_clipboard()
print(dataframe_nba)

lista_asignaturas = ['matematicas', 'historia', 'fisica']
lista_notas = [8,7,9]
diccionario = {'Asignaturas': lista_asignaturas, 'Notas': lista_notas}
print(diccionario)
dataframe_notas = pd.DataFrame(diccionario)
print(dataframe_notas)