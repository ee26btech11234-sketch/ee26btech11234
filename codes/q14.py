import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 60, 400)
y = 0.1 * x * (60 - x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label="Trajectory", color="blue")
plt.axvline(15, color="r", linestyle="--", label="Wall 1 (x=15, h=10)")
plt.axvline(45, color="r", linestyle="--", label="Wall 2 (x=45, h=10)")
plt.title("Question 14(a): Projectile Grazing Two Walls")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.grid(True)
plt.legend()
plt.show()
