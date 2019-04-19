import numpy as np

array1 = np.array([1,2,3,4])
sumarray = array1 + 4

print(sumarray)

list1 = [1,2,3,4]
list2 = [5,6,7,8]
lista_doble = (list1, list2)
array_doble = np.array(lista_doble)
print(array_doble)

result = array_doble * 5
print(result)