import numpy as np

arrayszeros = np.zeros(4)
print(arrayszeros)

elements = np.arange(10)
print(elements)

limits = np.arange(2,20,3)
print(limits)

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)
print(lista_doble)

array_doble = np.array(lista_doble)
print(array_doble)
print(array_doble.shape)
print(array_doble.dtype)