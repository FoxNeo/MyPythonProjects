import numpy as np

array1 = np.arange(6)

np.save('array1s', array1)
reuslt = np.load('array1s.npy')
print(reuslt)

array2 = np.arange(8)
np.savez('arrays', x=array1, y =array2)
array_restored = np.load('arrays.npz')
print(array_restored['x'])
print(array_restored['y'])

np.savetxt('mificheroarray.txt', array2, delimiter=',')
np.loadtxt('mificheroarray.txt', delimiter=',')
