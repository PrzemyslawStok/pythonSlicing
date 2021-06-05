import numpy as np
from matplotlib import pyplot as plot

print("Plot 3d")

x: np.ndarray = np.linspace(-1.0, 1.0, 200)
y: np.ndarray = np.sin(x)

figure = plot.figure(figsize=(10,10))

for i in range(25):
    plot.subplot(5,5,i+1)
    plot.plot(x,x**i)

plot.show()

figure = plot.figure(figsize=(5,5))
figure.add_subplot('111',projection='3d')

plot.show()