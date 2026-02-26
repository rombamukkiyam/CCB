import random

# ---------- Reaction update rules ----------
def fire_reaction(r, x1, x2, x3):
    if r == 1:      # R1: 2X1 + X2 -> 4X3
        return x1-2, x2-1, x3+4
    elif r == 2:    # R2: X1 + 2X3 -> 3X2
        return x1-1, x2+3, x3-2
    else:           # R3: X2 + X3 -> 2X1
        return x1+2, x2-1, x3-1


# ---------- Check stopping condition ----------
def check_outcome(x1, x2, x3):
    if x1 >= 150:
        return 1
    if x2 < 10:
        return 2
    if x3 > 100:
        return 3
    return 0


# ---------- Single stochastic trajectory ----------
def run_simulation():
    x1, x2, x3 = 110, 26, 55

    while True:

        # stop if any outcome reached
        outcome = check_outcome(x1, x2, x3)
        if outcome != 0:
            return outcome

        # compute propensities (given in problem)
        a1 = 0.5 * x1 * (x1 - 1) * x2
        a2 = x1 * x3 * (x3 - 1)
        a3 = 3 * x2 * x3

        total = a1 + a2 + a3

        # choose reaction probabilistically
        r = random.random() * total

        if r < a1:
            reaction = 1
        elif r < a1 + a2:
            reaction = 2
        else:
            reaction = 3

        # update state
        x1, x2, x3 = fire_reaction(reaction, x1, x2, x3)


# ---------- Monte Carlo estimation ----------
def estimate_probabilities(num_runs=10000):
    counts = [0, 0, 0, 0]   # index 1..3 used

    for _ in range(num_runs):
        outcome = run_simulation()
        counts[outcome] += 1

    p1 = counts[1] / num_runs
    p2 = counts[2] / num_runs
    p3 = counts[3] / num_runs

    return p1, p2, p3


# ---------- Run ----------
if __name__ == "__main__":
    runs = 20000
    p1, p2, p3 = estimate_probabilities(runs)

    print(f"Runs = {runs}")
    print(f"Pr(C1) ≈ {p1}")
    print(f"Pr(C2) ≈ {p2}")
    print(f"Pr(C3) ≈ {p3}")