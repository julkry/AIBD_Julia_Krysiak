# Julia Krysiak

import matplotlib.pyplot as plt
import numpy as np


# definicja funkcji
def f(x):
    return x ** 2 + 5


# przedziały
range1 = np.linspace(-1, 1, 100)
range2 = np.linspace(-6, 6, 100)
range3 = np.linspace(0, 5, 100)

y1 = f(range1)
y2 = f(range2)
y3 = f(range3)

# plot
_, ax = plt.subplots()
ax.plot(range1, y1, linewidth=2.0)
plt.show()

_, ax = plt.subplots()
ax.plot(range2, y2, linewidth=2.0)
plt.show()

_, ax = plt.subplots()
ax.plot(range3, y3, linewidth=2.0)
plt.show()
