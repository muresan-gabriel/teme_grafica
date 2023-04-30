import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.array([0, 0, 1, 1, 0.5, 0.5, 0.75, 0.75, 0.5, 0.5, 0])
y = np.array([0, 2, 2, 1.5, 1.5, 1, 1, 0.75, 0.75, 0, 0])

# Unghiul de rotație
theta = -np.pi / 4

R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

xy = np.vstack((x, y)).T
rotated_xy = np.dot(R, xy.T).T

# Vector de translație
tx = 1.5
ty = 1.5

translated_xy = rotated_xy + np.array([tx, ty])

plt.plot(x, y, 'r-', linewidth=2)

plt.plot(translated_xy[:, 0], translated_xy[:, 1], 'b-', linewidth=2)

plt.xlim(-3, 4)
plt.ylim(-3, 4)
plt.title('Poziție inițială și rotire + roto-translație')

plt.show()
