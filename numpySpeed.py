import timeit

import numpy as np
from numba import jit

@jit(nopython=True, cache=True)
def compileSpeed(arrayLength=100_000):
    A = np.arange(0, arrayLength)

    for i in range(arrayLength):
        A[i] = A[i] * A[i]

#@jit(nopython=True)
def function0():
    A = np.arange(0, 1000)

    for i in range(1000):
        A[i] = A[i] * A[i]


def speedNumpy(arrayLength=100_000):
    A = []

    startTime = timeit.default_timer()

    for i in range(arrayLength):
        A.append(i)

    for i in range(len(A)):
        A[i] = A[i] * A[i]

    endTime = timeit.default_timer()

    print(f"elapsed time: {(endTime - startTime):0.5f}s arrayLength:{arrayLength}")

    startTime = timeit.default_timer()

    B = np.arange(0, len(A))
    B = B * B

    endTime = timeit.default_timer()

    print(f"elapsed time numpy: {(endTime - startTime):0.5f}s")


speedNumpy(arrayLength=10_000_000)

for i in range(10):
    startTime = timeit.default_timer()
    function0()
    #compileSpeed(arrayLength=10_000_000)
    # compileSpeed.parallel_diagnostics(level=1)

    endTime = timeit.default_timer()
    print(f"numba time: {(endTime - startTime):0.5f}s")

