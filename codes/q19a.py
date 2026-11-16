import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5, 5))
plt.quiver(
    0,
    0,
    2,
    0,
    angles="xy",
    scale_units="xy",
    scale=1,
    color="blue",
    label="Force P",
)
plt.quiver(
    0,
    0,
    -1,
    1.732,
    angles="xy",
    scale_units="xy",
    scale=1,
    color="green",
    label="Force Q",
)
plt.quiver(
    0,
    0,
    -1,
    -1.732,
    angles="xy",
    scale_units="xy",
    scale=1,
    color="red",
    label="Force R",
)

plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.axhline(0, color="gray", linewidth=0.5)
plt.axvline(0, color="gray", linewidth=0.5)
plt.title("Question 19(a): Three Forces in Equilibrium")
plt.grid(True)
plt.legend()
plt.show()
