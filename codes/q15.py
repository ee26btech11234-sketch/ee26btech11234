import matplotlib.pyplot as plt

plt.figure(figsize=(4, 6))
plt.arrow(
    -0.1,
    0,
    0,
    2.5,
    head_width=0.08,
    head_length=0.1,
    fc="blue",
    ec="blue",
    label="Projection (u)",
)
plt.arrow(
    0.1,
    2.5,
    0,
    -2.5,
    head_width=0.08,
    head_length=0.1,
    fc="red",
    ec="red",
    label="Return",
)
plt.axhline(2.5, color="gray", linestyle="--", label="H = 50 m (v=0)")
plt.scatter([0], [0], color="black", zorder=5)
plt.text(0.1, -0.2, "Ground (y=0)")
plt.title("Question 15(a): Vertical Motion")
plt.xlim(-1, 1)
plt.ylim(-0.5, 3)
plt.grid(True)
plt.legend()
plt.show()
