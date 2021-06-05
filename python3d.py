import numpy as np
from matplotlib import pyplot as plot

print("Plot 3d")

x: np.ndarray = np.linspace(-1.0, 1.0, 100)
y: np.ndarray = np.sin(x)

plot.plot(x,y)
plot.show()