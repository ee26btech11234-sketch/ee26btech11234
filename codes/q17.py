import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(projection="3d")

t = np.linspace(-2, 2, 100)
x = 2 + 1 * t
y = -1 + 2 * t
z = -1 + 3 * t

ax.plot(x, y, z, label="Line: m = (1, 2, 3)", color="blue")
ax.scatter([2], [-1], [-1], color="red", s=50, label="Point (2, -1, -1)")
ax.set_title("Question 17(a): 3D Line Trajectory")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.grid(True)
ax.legend()
plt.show()
