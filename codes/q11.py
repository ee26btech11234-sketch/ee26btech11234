import matplotlib.pyplot as plt
import numpy as np

a = 1.0
x = np.linspace(0, 4 * a, 400)
y1 = np.sqrt(4 * a * x)
y2 = (x**2) / (4 * a)

plt.figure(figsize=(6, 4))
plt.plot(x, y1, label="y^2 = 4ax", color="blue")
plt.plot(x, y2, label="x^2 = 4ay", color="red")
plt.fill_between(x, y1, y2, color="gray", alpha=0.3, label="Enclosed Area")
plt.title("Question 11: Area Enclosed by Parabolas")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
