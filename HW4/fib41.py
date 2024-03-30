import time
import threading
import multiprocessing


def dynamic_fibonacci(n):
    F = []
    F.append(0)
    F.append(1)
    for i in range(2, n+1):
        F.append(F[i-1] + F[i-2])
    return F[n]

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def sync(fibonacci, n):
    start = time.time()
    for _ in range(10):
        fibonacci(n)
    end = time.time()
    return  end - start

def thread(fibonacci, n):
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=fibonacci, args=(n,))
        threads.append(thread)

    start = time.time()
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    end = time.time()

    return end - start

def process(fibonacci, n):
    processes = []
    for _ in range(10):
        process = multiprocessing.Process(target=fibonacci, args=(n,))
        processes.append(process)

    start = time.time()
    for process in processes:
        process.start()

    for process in processes:
        process.join()
    end = time.time()

    return end - start


if __name__ == "__main__":
    rn = 42
    dn = 42424
    with open("artifacts/4_1.txt", "w") as f:
        f.write("Рекурсивная функция Фибоначчи при n = 42.\n")
        f.write("Синхронный запуск: {}\n".format(sync(recursive_fibonacci, rn)))
        f.write("Запуск через потоки: {}\n".format(thread(recursive_fibonacci, rn)))
        f.write("Запуск через процессы: {}\n\n".format(process(recursive_fibonacci, rn)))
        f.write("Динамическая функция Фибоначчи при n = 42424.\n")
        f.write("Синхронный запуск: {}\n".format(sync(dynamic_fibonacci, dn)))
        f.write("Запуск через потоки: {}\n".format(thread(dynamic_fibonacci, dn)))
        f.write("Запуск через процессы: {}".format(process(dynamic_fibonacci, dn)))
