from multiprocessing import Pool
import time

def worker(n):
    return n ** 1000


if __name__ == '__main__':
    # Define the range of numbers
    numbers_range = range(100000)

    # Multiprocessing Pool
    start_time = time.time()
    with Pool(5) as p:
        pool_result = p.map(worker, numbers_range)
        multiprocessing_execution_time = time.time() - start_time

    print("Multiprocessing Pool took:", multiprocessing_execution_time, "seconds")

    # Serial processing
    start_time = time.time()
    serial_result = [worker(n) for n in numbers_range]
    serial_execution_time = time.time() - start_time

    print("Serial processing took:", serial_execution_time, "seconds")

# Multiprocessing Pool took: 3.358834981918335 seconds
# Serial processing took: 5.694896459579468 seconds
