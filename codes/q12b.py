import numpy as np
import matplotlib.pyplot as plt

N_sim = 100000
rng = np.random.default_rng(42)

bags = [
    ['W']*1 + ['B']*2 + ['R']*3,
    ['W']*2 + ['B']*1 + ['R']*1,
    ['W']*4 + ['B']*3 + ['R']*2
]

bag_counts = [0, 0, 0]
valid_draws = 0
for _ in range(N_sim):
    b_idx = rng.integers(0, 3)
    draw = rng.choice(bags[b_idx], size=2, replace=False)
    if set(draw) == {'W', 'R'}:
        bag_counts[b_idx] += 1
        valid_draws += 1

sim = [c / valid_draws for c in bag_counts]
theo = [9/34, 15/34, 10/34]

x = np.array([1, 2, 3])
plt.figure(figsize=(6, 4))
plt.stem(x - 0.05, theo, linefmt='b-', markerfmt='bo', basefmt=' ', label='Theoretical Posterior PMF')
plt.stem(x + 0.05, sim, linefmt='r--', markerfmt='rs', basefmt=' ', label='Simulated Posterior PMF')
plt.xticks(x, ['Bag I', 'Bag II', 'Bag III'])
plt.ylabel(r'$p_{B|E}(b|e)$')
plt.title('Posterior PMF Comparison: Bag Selection')
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()
