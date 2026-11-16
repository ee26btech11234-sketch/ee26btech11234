import numpy as np
import matplotlib.pyplot as plt

N_sim = 100000
rng = np.random.default_rng(42)
d1 = rng.integers(1, 7, size=N_sim)
d2 = rng.integers(1, 7, size=N_sim)

event = (d1 == d2) | ((d1 + d2) == 10)
sim = [np.mean(~event), np.mean(event)]
theo = [7/9, 2/9]

x = np.arange(2)
plt.figure(figsize=(5.5, 4))
plt.stem(x - 0.05, theo, linefmt='b-', markerfmt='bo', basefmt=' ', label='Theoretical PMF')
plt.stem(x + 0.05, sim, linefmt='r--', markerfmt='rs', basefmt=' ', label='Simulated PMF')
plt.xticks(x, ['X = 0 (Neither)', 'X = 1 (Doublet or Sum 10)'])
plt.ylabel('Probability')
plt.title('PMF Comparison: Single Throw of Two Dice')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
