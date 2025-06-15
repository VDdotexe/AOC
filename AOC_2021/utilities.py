def parsing_multi(file_):
    with open(file_, "r") as f:
        content = f.readlines()
    content = [i.replace("\n", "") for i in content]
    return content


def parsing_multi_ravi(file_):
    with open(file_, "r") as f:
        content = f.read()
    content = content.split("\n")
    return content


import multiprocessing
import time


def heavy_computation(x):
    total = 0
    for i in range(50_000_000):
        total += (x + i) % 7
    return total


if __name__ == "__main__":
    numbers = list(range(32))

    start_seq = time.time()
    results_seq = list(map(heavy_computation, numbers))
    end_seq = time.time()
    print("Sequential results:", results_seq)
    print("Sequential time:", end_seq - start_seq, "seconds")

    start_par = time.time()
    with multiprocessing.Pool() as pool:
        results_par = pool.map(heavy_computation, numbers)
    end_par = time.time()
    print("Parallel results:", results_par)
    print("Parallel time:", end_par - start_par, "seconds")
