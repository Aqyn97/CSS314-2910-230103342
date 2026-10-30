"""Experiment B: lock-protected shared counter under contention."""
import time
from multiprocessing import Process, Value, Lock, freeze_support

WORKER_COUNTS = (1, 2, 4)


def contended_worker(shared_counter, lock, iterations: int) -> None:
    for _ in range(iterations):
        with lock:
            shared_counter.value += 1


def run_contended(p: int, total_increments: int = 2_000_000) -> float:
    if total_increments % p != 0:
        raise ValueError('total_increments must be divisible by p')
    increments_per_worker = total_increments // p
    counter = Value('i', 0)
    lock = Lock()
    processes = [Process(target=contended_worker, args=(counter, lock, increments_per_worker)) for _ in range(p)]
    start = time.perf_counter()
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    elapsed = time.perf_counter() - start
    if any(process.exitcode != 0 for process in processes):
        raise RuntimeError('A worker process exited unsuccessfully')
    assert counter.value == total_increments, f'Counter mismatch: {counter.value}'
    return elapsed


def metrics(t1: float, tp: float, p: int) -> tuple[float, float]:
    speedup = t1 / tp
    e = (p / speedup - 1.0) / (p - 1.0)
    return speedup, e


if __name__ == '__main__':
    freeze_support()
    runtimes = {p: run_contended(p) for p in WORKER_COUNTS}
    for p, elapsed in runtimes.items():
        if p == 1:
            print(f'P={p} | Runtime={elapsed:.6f}s | Speedup=1.0000x | Karp-Flatt e=N/A')
        else:
            speedup, e = metrics(runtimes[1], elapsed, p)
            print(f'P={p} | Runtime={elapsed:.6f}s | Speedup={speedup:.4f}x | Karp-Flatt e={e:.4f}')
