import numpy as np
import os, psutil


#tworzymy macierz 2d o rozmiarach 10x10

A: np.ndarray = np.empty([100,100],dtype=np.ndarray)

#do tej macierzy przyporządkujemy macierze losowe o rozmiarach 100x100

for i in range(10):
    for j in range(10):
        A1: np.ndarray = np.random.random([1000,1000])
        A[i,j] = A1.astype(dtype="float64")

print(A)

#proszę zobaczyć ile program zajmuje w pamięci

process = psutil.Process(os.getpid())
print(f"Rozmiar pamięci: {process.memory_info()}")
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)

#proszę zminić typ macierzy losowej na uint8 i zobaczyć co dzieje się z pamięcią

#np.random.random([5,5], dtype="uint8")
