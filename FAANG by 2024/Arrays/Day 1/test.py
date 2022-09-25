import numpy as np

a = np.array([1,2,3,4,5])
for i in range(2,len(a)-1):
    a[i] = a[i+1]

del a[2]
print(a)    