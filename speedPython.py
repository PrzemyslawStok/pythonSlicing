import timeit

import numpy as np
from numba import jit, njit

def function0():
    A = np.arange(0, 1000_000)

    for i in range(len(A)):
        A[i] = A[i] * A[i]

@jit(nopython=True)
def function1():
    A = np.arange(0, 1000_000)

    for i in range(len(A)):
        A[i] = A[i] * A[i]

def function2():
    A = np.arange(0, 1000_000)
    A = A**2

@njit
def function3():
    A = np.arange(0, 1000_000)
    A = A**2

def functionSpeed(function, name: str, run_number = 10):
    for i in range(run_number):
        startTime = timeit.default_timer()
        function()
        endTime = timeit.default_timer()
        print(f"{name} time: {(endTime - startTime):0.5f}s")

functionSpeed(function0,"simple run",1)
functionSpeed(function1,"numba run",5)
functionSpeed(function2,"numpy run",5)
functionSpeed(function3,"numpy compile run",5)