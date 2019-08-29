import matplotlib.pyplot as plt
import numpy as np

vx0 = 2.5
v0y = 1000
g = (9.8)**2
pos = []

for t in np.arange(0.0,25.0, .01):
        sx = vx0 * t
        sy = (v0y * t) + ((.5)*(-g) * (t**2))
        pos.append((sx, sy))
        if sy < 0:
            break
x, y = zip(*pos)
plt.plot(x, y)
plt.show()