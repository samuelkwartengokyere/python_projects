import numpy as np

n = np.array(['10','20','30','40'])

print(n)
print(n.dtype,'\n')

n2 = n.astype('i')

print(n2.dtype)
print(n2)