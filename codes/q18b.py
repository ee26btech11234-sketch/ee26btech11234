import numpy as np
import matplotlib.pyplot as plt
from math import factorial, exp

N_sim = 100000
rng = np.random.default_rng(42)

claims = rng.binomial(1000, 0.001, size=N_sim)
k_vals = np.arange(0, 7)

theo = [exp(-1.0) * (1.0**k) / factorial(k) for k in k_vals]
sim = [np.mean(claims == k) for k in k_vals]

plt.figure(figsize=(6, 4))
plt.stem(k_vals - 0.08, theo, linefmt='b-', markerfmt='bo', basefmt=' ', label='Theoretical Poisson PMF')
plt.stem(k_vals + 0.08, sim, linefmt='r--', markerfmt='rs', basefmt=' ', label='Simulated PMF')
plt.xticks(k_vals)
plt.xlabel('Number of Accidents (k)')
plt.ylabel(r'$p_X(k)$')
plt.title('Poisson PMF Comparison: Policy Holder Accidents')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
