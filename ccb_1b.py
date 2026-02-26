import random
import numpy as np

# --------- reaction definitions ----------
# State S = [x1, x2, x3]

def reaction_weights(S):
    x1, x2, x3 = S

    if x1 < 2 or x2 < 1:
        w1 = 0
    else:
        w1 = 0.5 * x1 * (x1 - 1) * x2

    if x1 < 1 or x3 < 2:
        w2 = 0
    else:
        w2 = x1 * x3 * (x3 - 1)

    if x2 < 1 or x3 < 1:
        w3 = 0
    else:
        w3 = 3 * x2 * x3

    return [w1, w2, w3]


def apply_reaction(S, reaction):
    x1, x2, x3 = S

    if reaction == 0:      # R1: 2X1 + X2 -> 4X3
        return [x1 - 2, x2 - 1, x3 + 4]

    elif reaction == 1:    # R2: X1 + 2X3 -> 3X2
        return [x1 - 1, x2 + 3, x3 - 2]

    else:                  # R3: X2 + X3 -> 2X1
        return [x1 + 2, x2 - 1, x3 - 1]


# --------- one 7-step simulation ----------
def simulate_7_steps(initial_state):
    S = initial_state[:]

    for _ in range(7):
        weights = reaction_weights(S)
        total = sum(weights)

        if total == 0:
            break  # no reaction possible

        r = random.uniform(0, total)
        cumulative = 0

        for i, w in enumerate(weights):
            cumulative += w
            if r <= cumulative:
                S = apply_reaction(S, i)
                break

    return S


# --------- Monte Carlo experiment ----------
N = 10000
initial_state = [9, 8, 7]

final_states = np.array([simulate_7_steps(initial_state) for _ in range(N)])

# Means
mean_X1 = np.mean(final_states[:, 0])
mean_X2 = np.mean(final_states[:, 1])
mean_X3 = np.mean(final_states[:, 2])

# Variances
var_X1 = np.var(final_states[:, 0])
var_X2 = np.var(final_states[:, 1])
var_X3 = np.var(final_states[:, 2])

print("After 7 steps:")
print(f"Mean  -> X1={mean_X1:.2f}, X2={mean_X2:.2f}, X3={mean_X3:.2f}")
print(f"Var   -> X1={var_X1:.2f}, X2={var_X2:.2f}, X3={var_X3:.2f}")