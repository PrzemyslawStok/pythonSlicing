import timeit

import numpy as np
from numba import jit

#@jit(nopython=True)
def function0():
    A = np.arange(0, 1000)

    for i in range(1000):
        A[i] = A[i] * A[i]

def functionSpeed(function, name: str):
    for i in range(10):
        startTime = timeit.default_timer()
        function()
        endTime = timeit.default_timer()
        print(f"{name} time: {(endTime - startTime):0.5f}s")

functionSpeed(function0,"simple run")