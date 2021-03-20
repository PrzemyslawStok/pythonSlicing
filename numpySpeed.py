import timeit

import numpy as np
from numba import jit

def compileSpeed(arrayLength = 1000_00):
    startTime = timeit.default_timer()
    A = []

    for i in range(arrayLength):
        A.append(i)

    for i in range(len(A)):
        A[i] = A[i] * A[i]

    endTime = timeit.default_timer()

    print(f"numba time: {(endTime - startTime):0.5f}s")



def speedNumpy():
    A = []

    startTime = timeit.default_timer()

    for i in range(1000_000_0):
        A.append(i)

    for i in range(len(A)):
        A[i] = A[i] * A[i]

    endTime = timeit.default_timer()

    print(f"elapsed time: {(endTime - startTime):0.5f}s")

    startTime = timeit.default_timer()

    B = np.arange(0, len(A))
    B = B * B

    endTime = timeit.default_timer()

    print(f"elapsed time numpy: {(endTime - startTime):0.5f}s")

speedNumpy()

for i in range(10):
    compileSpeed()

