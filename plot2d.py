import numpy as np
from matplotlib import pyplot as plot


def plotFunction(x: np.ndarray, y: np.ndarray):
    plot.plot(x, y)


x: np.ndarray = np.linspace(-1.0, 1.0, 100)
y: np.ndarray = np.sin(x)

# print(x)

figure = plot.figure(figsize=(5, 5))
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
    plot.gca().axes.xaxis.set_visible(False)
    plot.gca().axes.yaxis.set_visible(False)
    plot.plot(x, y)

plot.show()

figure, ax = plot.subplots(5, 5)
print(np.shape(ax))

for i in range(0, 5):
    for j in range(0, 5):
        y = x ** ((i + 1) * (j + 1))
        ax[i, j].plot(x, y)


plot.show()

# proszę narysować obrazki dla x, x^2 ... x^5
# proszę narysować dwa wykresy zbiorcze
