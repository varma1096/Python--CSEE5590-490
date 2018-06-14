import numpy as np
array_t=np.random.randint(0,10,(10,10)) # Creating the
print(array_t)
min,max = array_t.min(axis=1),array_t.max(axis=1)
print("Minimum number of 10 size Array is",min)
print("Maximum Elements of 10 size Array is",max)