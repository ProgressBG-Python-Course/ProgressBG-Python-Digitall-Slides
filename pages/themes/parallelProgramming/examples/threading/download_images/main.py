import time
import asyncio

from lib.common.data import URLS
import lib.sync_solution as sync_solution
import lib.threading_solution as threading_solution
import lib.async_solution as async_solution


OUTPUT_DIR = './downloads/'

def sync_download():
    t1_start = time.perf_counter()
    sync_solution.download_all(URLS, OUTPUT_DIR)
    t1_stop = time.perf_counter()
    print(f'Total time sync_download: {t1_stop - t1_start}')

async def async_download():
    t1_start = time.perf_counter()
    await async_solution.download_all(URLS, OUTPUT_DIR)
    t1_stop = time.perf_counter()
    print(f'Total time async_download: {t1_stop - t1_start}')


def threading_download():
    t1_start = time.perf_counter()
    threading_solution.download_all(URLS, OUTPUT_DIR)
    t1_stop = time.perf_counter()
    print(f'Total time threading_download: {t1_stop - t1_start}')


def threading_pool_download():
    t1_start = time.perf_counter()
    threading_solution.download_all_pool(URLS, OUTPUT_DIR)
    t1_stop = time.perf_counter()
    print(f'Total time threading_pool_download: {t1_stop - t1_start}')



if __name__=="__main__":
    # sync_download()
    threading_download()
    # threading_pool_download()
    # asyncio.run(async_download())