import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(5, 5))

# Sphere cross-section (Radius = sqrt(8) ≈ 2.828, Center = (1, 1))
circle = plt.Circle(
    (1, 1), 2.828, color="blue", fill=False, lw=2, label="Sphere Cross-section"
)
ax.add_patch(circle)
ax.plot(
    [-2, 4], [3.828, 3.828], color="red", lw=2, label="Plane: x+y+z = √3λ"
)
ax.scatter([1], [1], color="black", zorder=5, label="Center (1, 0, 1)")

ax.set_xlim(-3, 5)
ax.set_ylim(-3, 6)
ax.set_title("Question 18(a): Sphere and Tangent Plane")
ax.grid(True)
ax.legend()
plt.show()
