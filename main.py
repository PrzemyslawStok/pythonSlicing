import numpy as np
from numpySpeed import speedNumpy

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print(A[5:10])

#print(A[-2:])
#print(A[0:-2])

# speedNumpy()

B = np.reshape(np.arange(0, 25), [5, -1])

print(B)
print("*****************************")

print(B[0:3,:])

#print(f"shape(B): {np.shape(B)}")
