import numpy as np

array = np.arange(0,11)
print(array)

cloneArray = array.copy()
print(cloneArray)

array2 = np.array(([1,2,3], [4,5,6],[7,8,9]))

print(array2)

print(array2[1][0]) #4
