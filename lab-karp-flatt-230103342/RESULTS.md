# Karp–Flatt Practice Lab Results

Student ID: 230103342  
Branch: `practice-230103342`  
Hardware: MacBook Air M2, 8 logical CPU cores (confirm with `python3 -c "import os; print(os.cpu_count())"`)  
Environment: macOS, Python 3.x (record exact version with `python3 --version`)

## Empirical measurements

Run the three scripts on your own machine and replace `PENDING` with the values printed in the terminal. Do not substitute expected/example values for measured values.

| Experiment | T1 (s) | T2 (s) | T4 (s) | Speedup S2 | Speedup S4 | e(2) | e(4) | Diagnosis |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A: Serial tail | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Fixed 0.40-second sequential pause |
| B: Lock contention | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Shared counter plus lock per increment |
| C: Private state | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | PENDING | Local accumulation, one final reduction |

## Calculations

For worker count `p`:

- `S(p) = T1 / Tp`
- `e(p) = ((p * Tp / T1) - 1) / (p - 1)` for `p >= 2`
- `E(p) = S(p) / p`, where efficiency is expressed as a proportion; multiply by 100 for percent
- Instructor check A: `0.80 <= e(4) / e(2) <= 1.25` when `e(2)` is nonzero
- Instructor check B: `T4 > T1` and `e(4) > e(2)`
- Instructor check C: `T4 < T1` and `E(4) > 0.70`

## Discussion

Experiment A includes an intentional 0.40-second serial pause. Its expected symptom is a relatively stable positive Karp–Flatt serial fraction as the worker count rises. Measured values still depend on work duration and process startup costs.

Experiment B acquires a process-shared mutex for each counter increment. Multiple workers compete for the same lock and shared memory location. This adds synchronization and inter-core communication costs. An increase in Karp–Flatt e with worker count is consistent with contention.

Experiment C avoids synchronization in the hot loop. Each process counts in its own local variable, and the parent combines the results once. This reduces coordination overhead, though CPython loop overhead, process startup, and the computer's scheduling may prevent ideal scaling. Record observed values even if they differ from the handout's expectations.

## Verification

- [ ] Confirm CPU core count and Python version
- [ ] Run A, B and C using actual machine benchmarks
- [ ] Replace all `PENDING` cells with real values
- [ ] Calculate the instructor's rubric checks using measured values
- [ ] Review the code before making local commits and pushing
