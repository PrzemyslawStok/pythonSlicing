import numpy as np
from matplotlib import pyplot as plot


def plotFunction(x: np.ndarray, y: np.ndarray):
    plot.plot(x, y)


x: np.ndarray = np.linspace(-1.0, 1.0, 100)
y: np.ndarray = np.sin(x)

# print(x)

plot.figure(figsize=(5, 5))
plot.plot(x, y)
# plot.show()

plot.plot(x, y + x)
plot.show()

# for i in range(1, 5):
#    y = x ** i
#    plotFunction(x, y)
#    plot.show()

for i in range(1, 26):
    y = x ** i
    plot.subplot(5, 5, i)
    plot.plot(x, y)

plot.show()

# proszę narysować obrazki dla x, x^2 ... x^5
