"""Experiment A: fixed serial pause with parallel compute work."""
import math
import time
from multiprocessing import Pool, freeze_support

WORKER_COUNTS = (1, 2, 4)


def heavy_math(n: int) -> float:
    return sum(math.sin(i) * math.cos(i) for i in range(1, n))


def run_experiment(workers: int, total_chunks: int = 16, chunk_size: int = 2_000_000) -> float:
    start = time.perf_counter()
    time.sleep(0.40)
    with Pool(processes=workers) as pool:
        pool.map(heavy_math, [chunk_size] * total_chunks)
    return time.perf_counter() - start


def metrics(t1: float, tp: float, workers: int) -> tuple[float, float]:
    speedup = t1 / tp
    karp_flatt = (workers / speedup - 1.0) / (workers - 1.0)
    return speedup, karp_flatt


if __name__ == '__main__':
    freeze_support()
    runtimes = {p: run_experiment(p) for p in WORKER_COUNTS}
    for p, elapsed in runtimes.items():
        if p == 1:
            print(f'P={p} | Runtime={elapsed:.6f}s | Speedup=1.0000x | Karp-Flatt e=N/A')
        else:
            speedup, e = metrics(runtimes[1], elapsed, p)
            print(f'P={p} | Runtime={elapsed:.6f}s | Speedup={speedup:.4f}x | Karp-Flatt e={e:.4f}')
