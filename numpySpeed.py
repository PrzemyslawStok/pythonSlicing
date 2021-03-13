import timeit

import numpy as np


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
