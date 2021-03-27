import numpy as np
from matplotlib import pyplot as plot

x: np.ndarray = np.linspace(-10, 10, 100)
y: np.ndarray = np.sin(x)

print(x)

plot.plot(x,y)
plot.show()
