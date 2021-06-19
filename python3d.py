import numpy as np
from matplotlib import pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

from student import student as st

print("Plot multiplot 2d")

x: np.ndarray = np.linspace(-1.0, 1.0, 200)
y: np.ndarray = np.sin(x)

figure = plot.figure(figsize=(10, 10))

for i in range(25):
    plot.subplot(5, 5, i + 1)
    plot.plot(x, x ** i)

plot.show()

print("Plot 3d - funkcja jednowymiarowa")

figure: plot.Figure = plot.figure(figsize=(5, 5))
axes: Axes3D = figure.add_subplot(111, projection='3d')

x: np.ndarray = np.linspace(0, 1.0, 2)
y: np.ndarray = np.linspace(0, 1.0, 2)

z = x**2+y
#plot.plot(x,y,z)

noPoints = 1000

def f1(noPoints):
    X = np.random.random(noPoints)
    Y = np.random.random(noPoints)
    Z = np.random.random(noPoints)
    return X,Y,Z

X,Y,Z = f1(100)

#axes.scatter(X,Y,Z)

#Zad.1 Proszę wygenerować trzy macierze z losowymi punktami w przestrzeni x,y,z
#Proszę utworzyć funkcję, która zwraca trzy macierze jednocześnie

plot.show()

figure: plot.Figure = plot.figure(figsize=(5, 5))
axes: Axes3D = figure.add_subplot(111, projection='3d')

x: np.ndarray = np.linspace(-10, 10, 1000)
y: np.ndarray = np.linspace(-10, 10, 1000)

print(x)
print(y)

X,Y = np.meshgrid(x,y)
Z = np.sin(np.sqrt(X*Y))

#axes.scatter(X,Y,Z)

axes.plot_surface(X,Y,Z,color='b')

plot.show()

student0: st = st("Przemysław","Stoklosa")
student0.print()

print(student0.name)