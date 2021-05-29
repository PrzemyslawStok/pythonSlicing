import numpy as np
import os, psutil

#Zad.1

#proszę utowrzyć macierz o rozmiarze 1000x1000 i wypełnić ją libami od 0 do 99999
#proszę sprawdzić rozmiar macierzy dla typów float64 i uint32

A = np.arange(0,1000000,dtype="uint32")
print(A)
B = np.reshape(A,[1000,-1])
print(f"Maksymalna liczba: {np.max(A)}")
print(B)



#proszę sprawdzić ile zajmuje w pamięci macierz B