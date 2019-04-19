import numpy as np

array = np.arange(15).reshape((3,5))
print(array)

print(array[1][1])

array_tras = array.T
print(array_tras)