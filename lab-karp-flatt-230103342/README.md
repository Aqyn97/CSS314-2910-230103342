# Empirical Scalability Diagnostics: Karp–Flatt Metric

Student ID: **230103342**

This solution follows the instructor's three-part Python multiprocessing lab. The scripts have no third-party dependencies.

## Run on macOS

```bash
python3 --version
python3 -c "import os; print(f'Execution Cores: {os.cpu_count()}')"
python3 exp_a_serial.py
python3 exp_b_contention.py
python3 exp_c_fixed.py
```

Use a terminal on your Mac. Each program reports its measured `T1`, `T2`, `T4`, speedup and Karp–Flatt estimates. Copy the outputs into `RESULTS.md`.

## Set up the assigned remote repository

The handout instructs students to clone an **assigned** course repository. Use the assignment URL supplied by your instructor, rather than creating an unrelated GitHub repository unless your instructor explicitly allows it.

```bash
git clone <ASSIGNED_REPO_URL> lab-karp-flatt
cd lab-karp-flatt
git checkout -b practice-230103342
```

Copy the prepared `.py` scripts, `RESULTS.md`, and `README.md` into the cloned folder. Review each file and save actual benchmark readings before committing.

Suggested commit sequence, if your instructor requires checkpoints:

```bash
git add exp_a_serial.py
git commit -m "Part 1: Experiment A complete"
git add exp_b_contention.py
git commit -m "Part 2: Captured lock contention pathology and Karp-Flatt surge"
git add exp_c_fixed.py RESULTS.md README.md
git commit -m "Part 3 & 4: Completed privatization fix and verified RESULTS.md"
git push -u origin practice-230103342
```

You control the commit and push. No remote changes have been made.
