import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 400)
x = x[x != 0]
y = (np.exp(x) - 1) / np.sqrt(1 - np.cos(x))

plt.figure(figsize=(6, 4))
plt.plot(x[x > 0], y[x > 0], "b-", label="Right branch")
plt.plot(x[x < 0], y[x < 0], "b-", label="Left branch")
plt.axhline(np.sqrt(2), color="r", linestyle="--", label="y = √2")
plt.axhline(-np.sqrt(2), color="g", linestyle="--", label="y = -√2")
plt.title("Question 1: Discontinuity at x = 0")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
