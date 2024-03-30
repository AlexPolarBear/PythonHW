import math
import time
import logging
import multiprocessing
from concurrent import futures


def integrate_thread(f, a, b, *, n_jobs=1, n_iter=1000):
    step = (b - a) / n_iter
    with futures.ThreadPoolExecutor(n_jobs) as executor:
        tasks = [executor.submit(f, a + i * step) for i in range(n_iter)]
    acc = 0
    for task in tasks:
        acc += task.result() * step
    return acc

def integrate_processes(f, a, b, *, n_jobs=1, n_iter=1000):
    step = (b - a) / n_iter
    with futures.ProcessPoolExecutor(n_jobs) as executor:
        tasks = [executor.submit(f, a + i * step) for i in range(n_iter)]
    acc = 0
    for task in tasks:
        acc += task.result() * step
    return acc

def thread(n_jobs_list):
    times_thread = []
    for n_jobs in n_jobs_list:
        start = time.time()
        integrate_thread(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        end = time.time()
        times_thread.append(end - start)
    return times_thread

def process(n_jobs_list):
    times_process = []
    for n_jobs in n_jobs_list:
        start = time.time()
        integrate_processes(math.cos, 0, math.pi / 2, n_jobs=n_jobs)
        end = time.time()
        times_process.append(end - start)
    return times_process


if __name__ == "__main__":
    logging.basicConfig(filename="artifacts/4_2.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    cpu_num = multiprocessing.cpu_count()
    n_jobs_list = [1, 2, 4, 8, 16] if cpu_num >= 8 else [1, 2, 4]

    times_thread = thread(n_jobs_list)
    times_process = process(n_jobs_list)

    logging.info("Сравнение времени выполнения для ThreadPoolExecutor:")
    for n_jobs, time in zip(n_jobs_list, times_thread):
        logging.info("n_jobs=%d, время=%f", n_jobs, time)

    logging.info("Сравнение времени выполнения для ProcessPoolExecutor:")
    for n_jobs, time in zip(n_jobs_list, times_process):
        logging.info("n_jobs=%d, время=%f", n_jobs, time)