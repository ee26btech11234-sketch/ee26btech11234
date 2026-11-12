import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 400)
y = x / (1 + x**2)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label="f(x) = x / (1 + x^2)", color="blue")
plt.axvline(-1, color="r", linestyle="--", label="x = -1 (Min)")
plt.axvline(1, color="g", linestyle="--", label="x = 1 (Max)")
plt.title("Question 5: Intervals of Increase and Decrease")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
