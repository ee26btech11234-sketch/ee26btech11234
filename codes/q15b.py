import numpy as np
import matplotlib.pyplot as plt

def MC(x):
    return 300 - 20*x + x**2

def dMC(x):
    return -20 + 2*x

def d2MC(x):
    return 2.0

x0 = 0.0
x1 = x0 - dMC(x0) / d2MC(x0)

x_vals = np.linspace(0, 20, 200)
plt.figure(figsize=(6, 4))
plt.plot(x_vals, MC(x_vals), 'b-', linewidth=2, label=r'$MC(x) = 300 - 20x + x^2$')
plt.scatter([x0, x1], [MC(x0), MC(x1)], color='red', zorder=5)
plt.annotate(f'Start $x_0={x0:.0f}$', (x0+0.4, MC(x0)-10))
plt.annotate(f'Min $x_1={x1:.0f}, MC={MC(x1):.0f}$', (x1-2.5, MC(x1)+12))
plt.xlabel('Output (x)')
plt.ylabel('Marginal Cost MC(x)')
plt.title('Marginal Cost Minimization via Newton-Raphson')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
