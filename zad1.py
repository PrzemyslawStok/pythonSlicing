import numpy as np
import os, psutil


#tworzymy macierz 2d o rozmiarach 10x10

A: np.ndarray = np.empty([10,10],dtype=np.ndarray)

#do tej macierzy przyporządkujemy macierze losowe o rozmiarach 100x100

for i in range(10):
    for j in range(10):
        A[i,j] = 1

print(A)

#proszę zobaczyć ile program zajmuje w pamięci

process = psutil.Process(os.getpid())
print(f"Rozmiar pamięci: {process.memory_info().rss}B")

#proszę zminić typ macierzy losowej na uint8 i zobaczyć co dzieje się z pamięcią

#np.random.random([5,5], dtype="uint8")