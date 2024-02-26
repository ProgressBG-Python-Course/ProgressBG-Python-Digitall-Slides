import time
import asyncio

from lib.data import URLS
from lib import sync_solution, threading_solution, async_solution

OUTPUT_DIR = './downloads/'

def sync_download():
    t1_start = time.perf_counter()
    sync_solution.download_all(URLS, OUTPUT_DIR)
    t1_stop = time.perf_counter()
    print(f'Total time sync_solution: {t1_stop - t1_start}')

async def async_download():
    t1_start = time.perf_counter()
    await async_solution.download_all(URLS, OUTPUT_DIR)
    t1_stop = time.perf_counter()
    print(f'Total time async_solution: {t1_stop - t1_start}')


def threading_download():
    t1_start = time.perf_counter()
    threading_solution.download_all(URLS, OUTPUT_DIR)
    t1_stop = time.perf_counter()
    print(f'Total time threading_solution: {t1_stop - t1_start}')


if __name__=="__main__":
    sync_download()
    threading_download()
    asyncio.run(async_download())