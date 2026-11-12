import matplotlib.pyplot as plt
import numpy as np

A = np.array([0, 0])
B = np.array([3, 0])
C = np.array([1.5, 2.598])

plt.figure(figsize=(5, 5))
plt.plot([A[0], B[0]], [A[1], B[1]], "k-", lw=2, label="c")
plt.plot([B[0], C[0]], [B[1], C[1]], "k-", lw=2, label="a")
plt.plot([C[0], A[0]], [C[1], A[1]], "k-", lw=2, label="b")
plt.text(1.5, -0.3, "c", fontsize=12)
plt.text(2.4, 1.4, "a", fontsize=12)
plt.text(0.6, 1.4, "b", fontsize=12)
plt.title("Question 12(a): Triangle Vector Representation")
plt.xlim(-1, 4)
plt.ylim(-1, 3.5)
plt.grid(True)
plt.legend()
plt.show()
