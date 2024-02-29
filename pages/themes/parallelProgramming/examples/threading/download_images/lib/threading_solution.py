import threading
import concurrent.futures
from typing import List

from lib.common.utils import download_image, make_filename, write_to_file

def download_one(url, output_dir):
    img_bytes = download_image(url)
    if img_bytes:
        filename = make_filename(url)
        write_to_file(output_dir + filename, img_bytes)

def download_all(urls:List[str], output_dir:str)->None:
    # Create and start all threads
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_one, args=(url, output_dir))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

def download_all_pool(urls:List[str], output_dir:str)->None:
    """ manage threads automatically. It handles thread creation, scheduling, and resource management internally."""
    with concurrent.futures.ThreadPoolExecutor() as executor:
           executor.map(lambda url: download_one(url, output_dir), urls)




