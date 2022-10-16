import time
import math
import numpy as np
import matplotlib.pyplot as plt

def drawCircle(x, y, z, r):
	theta = np.arange(0, 2*np.pi, 0.1)
	rx = x + r * np.cos(theta)
	ry = y + r * np.sin(theta)

	rx = rx.reshape(rx.shape[0], 1)
	ry = ry.reshape(ry.shape[0], 1)
	return rx, ry, z


fig = plt.figure(figsize=(5,5))
ax00 = fig.add_subplot(111, projection="3d")

for i in range(1, 5):
	x, y, z = drawCircle(0, 0, i, i)
	
	#ax00.cla()
	#ax00.title.set_text('Dataset')

	ax00.scatter(x, y, z, c=x, cmap="plasma")
plt.show()

