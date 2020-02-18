import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)

l = 10
m = 5
n = 5

x = np.outer(phi, np.cos(theta)) + np.outer(l, theta**0.5)
y = np.outer(phi, np.sin(theta)) + np.outer(m,theta**0.5)
z =np.outer( n, theta**0.5)

ax.plot_surface(x, y, z, color='b')
plt.show() 
