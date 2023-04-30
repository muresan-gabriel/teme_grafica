import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Coordonatele inițiale
x = np.array([0, 0, 1, 1, 0.5, 0.5, 0.75, 0.75, 0.5, 0.5, 0])
y = np.array([0, 2, 2, 1.5, 1.5, 1, 1, 0.75, 0.75, 0, 0])

# Afișare F inițial
plt.plot(x, y, 'k-', linewidth=2, label='Inițial')

# Unghiul de rotație
theta = np.pi/2 # pi / 2 = 90deg

c, s = np.cos(theta), np.sin(theta)
R = np.array(((c, -s), (s, c)))

coords = np.array([x, y]).T
rotated_coords = np.dot(R, coords.T).T

plt.plot(rotated_coords[:,0], rotated_coords[:,1], 'r-', linewidth=2, label='După modificare')

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.title('Litera F')

plt.legend()
plt.show()
