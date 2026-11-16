import numpy as np
import matplotlib.pyplot as plt
from math import comb

N_sim = 100000
bag = np.array(['R']*8 + ['W']*3 + ['B']*9)

p_blue = comb(9, 3) / comb(20, 3)
p_diff = (comb(8, 1) * comb(3, 1) * comb(9, 1)) / comb(20, 3)
p_other = 1.0 - (p_blue + p_diff)
theo = [p_blue, p_diff, p_other]

rng = np.random.default_rng(42)
counts = [0, 0, 0]
for _ in range(N_sim):
    draw = rng.choice(bag, size=3, replace=False)
    if np.all(draw == 'B'):
        counts[0] += 1
    elif len(set(draw)) == 3:
        counts[1] += 1
    else:
        counts[2] += 1
sim = [c / N_sim for c in counts]

x = np.arange(3)
plt.figure(figsize=(6, 4))
plt.stem(x - 0.06, theo, linefmt='b-', markerfmt='bo', basefmt=' ', label='Theoretical PMF')
plt.stem(x + 0.06, sim, linefmt='r--', markerfmt='rs', basefmt=' ', label='Simulated PMF')
plt.xticks(x, ['All Blue', 'Different Colors', 'Other'])
plt.ylabel('Probability')
plt.title('PMF Comparison: Drawing 3 Balls')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
