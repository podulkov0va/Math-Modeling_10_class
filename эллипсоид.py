import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)

a = 10
b = 5
c = 5

x = a * np.outer(np.cos(phi), np.sin(theta))
y = b * np.outer(np.sin(phi), np.sin(theta))
z =np.outer( c , np.cos(theta))

ax.plot_surface(x, y, z, color='b')
plt.show() 