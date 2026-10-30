"""Experiment C: private process-local increments followed by one reduction."""
import time
from multiprocessing import Pool, freeze_support

WORKER_COUNTS = (1, 2, 4)


def private_worker(iterations: int) -> int:
    local_sum = 0
    for _ in range(iterations):
        local_sum += 1
    return local_sum


def run_privatized(p: int, total_increments: int = 20_000_000) -> float:
    if total_increments % p != 0:
        raise ValueError('total_increments must be divisible by p')
    tasks = [total_increments // p] * p
    start = time.perf_counter()
    with Pool(processes=p) as pool:
        results = pool.map(private_worker, tasks)
    total = sum(results)
    elapsed = time.perf_counter() - start
    assert total == total_increments, f'Incorrect total: {total}'
    return elapsed


def metrics(t1: float, tp: float, p: int) -> tuple[float, float, float]:
    speedup = t1 / tp
    e = (p / speedup - 1.0) / (p - 1.0)
    efficiency = speedup / p
    return speedup, e, efficiency


if __name__ == '__main__':
    freeze_support()
    runtimes = {p: run_privatized(p) for p in WORKER_COUNTS}
    for p, elapsed in runtimes.items():
        if p == 1:
            print(f'P={p} | Runtime={elapsed:.6f}s | Speedup=1.0000x | Karp-Flatt e=N/A | Efficiency=100.00%')
        else:
            speedup, e, efficiency = metrics(runtimes[1], elapsed, p)
            print(f'P={p} | Runtime={elapsed:.6f}s | Speedup={speedup:.4f}x | Karp-Flatt e={e:.4f} | Efficiency={efficiency:.2%}')
