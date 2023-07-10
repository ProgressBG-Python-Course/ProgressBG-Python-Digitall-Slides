import time
from lib.data import URLS
from lib import sync_solution, threading_solution

OUTPUT_DIR = './downloads/'

def sync_download():
	t1_start = time.perf_counter()
	sync_solution.download_all(URLS, OUTPUT_DIR)
	t1_stop = time.perf_counter()
	print(f'Total time sync_solution: {t1_stop - t1_start}')

def async_download():
	t1_start = time.perf_counter()
	ssync_solution.download_all(URLS, OUTPUT_DIR)
	t1_stop = time.perf_counter()
	print(f'Total time async_solution: {t1_stop - t1_start}')


def threading_download():
	t1_start = time.perf_counter()
	threading_solution.download_all(URLS, OUTPUT_DIR)
	t1_stop = time.perf_counter()
	print(f'Total time threading_solution: {t1_stop - t1_start}')


# sync_download()
threading_download()