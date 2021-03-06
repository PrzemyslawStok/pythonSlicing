import timeit

import numpy as np
from numba import jit, njit, prange

import tensorflow as ts
from matplotlib import pyplot as plot

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
    A = A ** 2


@njit
def function3():
    A = np.arange(0, 1000_000)
    A = A ** 2


#@njit(parallel=True)
def function_parallel():
    A = np.arange(0, 1000_000)

    for i in prange(len(A)):
        A[i] = A[i] * A[i]


def functionSpeed(function, name: str, run_number=10):
    for i in range(run_number):
        startTime = timeit.default_timer()
        function()
        endTime = timeit.default_timer()
        print(f"{name} time: {(endTime - startTime):0.5f}s")


mnistData = ts.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = mnistData.load_data()

imageNo = 1

plot.imshow(training_images[imageNo])
plot.show()

print(f"na obrazku numer {imageNo} znajduje się cyfra: {training_labels[imageNo]}")


#functionSpeed(function0, "simple run", 1)
#functionSpeed(function1, "numba run", 5)
#functionSpeed(function2, "numpy run", 5)
#functionSpeed(function3, "numpy compile run", 5)
#functionSpeed(function_parallel, "parallel numba run", 5)

print("---------------------------")

#function_parallel.parallel_diagnostics(level=4)

# function1.inspect_types()


