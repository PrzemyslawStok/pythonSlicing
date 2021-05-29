import numpy as np


# from numpySpeed import speedNumpy

def multiparam(x: float, y: float) -> (float, float, float, np.array, np.array):
    A1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    A2 = np.reshape(A1, [-1, 2])
    return 1.0, 2.0, 3.0, A1, A2


# print(f"{multiparam()}")
a, b, c, d, e = multiparam(1.0, 2.0)

print(f"------------------------------------")

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
A1 = np.empty([5, 5], dtype=np.ndarray)
B = np.arange(0, 10000)
B = np.reshape(B, [100, -1])

M = np.random.random()

print(A[1:6])

print(A[-5:])

print(A[:-2])
print(A[-2:])

# speedNumpy()

B = np.reshape(np.arange(0, 25), [5, -1])

print(B)

print("*****************************")

print(B[2:5, 2:5])

# print(f"shape(B): {np.shape(B)}")
