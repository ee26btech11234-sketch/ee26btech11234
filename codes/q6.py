import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi / 2, 100)
y = (np.sin(x) ** 2) / (np.sin(x) + np.cos(x))

xi = np.linspace(0, np.pi / 2, 5)
yi = (np.sin(xi) ** 2) / (np.sin(xi) + np.cos(xi))

plt.figure(figsize=(6, 4))
plt.plot(x, y, label="f(x)", color="blue")
plt.plot(xi, yi, "ro-", label="Trapezoidal Nodes (N=4)")
plt.fill_between(xi, yi, color="skyblue", alpha=0.4)
plt.title("Question 6: Trapezoidal Rule Approximation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
