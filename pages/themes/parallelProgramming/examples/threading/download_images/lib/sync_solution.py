import re
import requests
from typing import List

from lib.common.utils import download_image, make_filename, write_to_file

def download_all(urls:List[str], output_dir:str)->None:
	for url in urls:
		img_bytes = download_image(url)
		if img_bytes:
			filename = make_filename(url)
			write_to_file(output_dir + filename, img_bytes)

