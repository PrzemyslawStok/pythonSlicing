import numpy as np
from matplotlib import pyplot as plot

def plotFunction(x: np.ndarray, y: np.ndarray):
    plot.plot(x, y)
    plot.show()


x: np.ndarray = np.linspace(-10, 10, 100)
y: np.ndarray = np.sin(x)

print(x)

plot.plot(x,y)
plot.show()

plot.plot(x,y+x)
plot.show()

for i in range(5):
    pass

#proszę narysować obrazki dla x, x^2 ... x^5

