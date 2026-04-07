def fibonacci_crn(F0: int, F1: int, num_steps: int = 12) -> int:
  
    A, B, T, Bp, C = F0, F1, 0, 0, num_steps

    print(f"\nF0={F0}, F1={F1} | {num_steps} steps")
    print(f"{'Step':>4}  {'[A]':>6}  {'[B]':>7}  {'[C]':>4}")
    print(f"{'─'*30}")
    print(f"{'0':>4}  {A:>6}  {B:>7}  {C:>4}  ← initial")

    for s in range(1, num_steps + 1):
        T  += A;  A = 0          # R1
        A  += B; Bp += B; B = 0  # R2
        B  += T;  T = 0          # R3
        B  += Bp; Bp = 0         # R4
        C  -= 1                   # R5
        print(f"{s:>4}  {A:>6}  {B:>7}  {C:>4}  ← F({s})={A}")

    print(f"\nResult: [A] = {A}  (C={C}, halted)")
    return A



r1 = fibonacci_crn(F0=0, F1=1)
assert r1 == 144, f"Expected 144, got {r1}"
print(f" F(12) from (0,1) = {r1}")


r2 = fibonacci_crn(F0=3, F1=7)
assert r2 == 1275, f"Expected 1275, got {r2}"
print(f" F(12) from (3,7) = {r2}")