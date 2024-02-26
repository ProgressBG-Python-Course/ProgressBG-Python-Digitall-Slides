import re
import aiohttp
import asyncio
from typing import List

async def download_image(session: aiohttp.ClientSession, url: str) -> bytes:
    # print(f'Downloading {url}')
    async with session.get(url) as response:
        if response.status == 200:
            return await response.read()
        else:
            print(f'Failed to download {url}: {response.status}')

async def write_to_file(filename: str, img_bytes: bytes) -> None:
    with open(filename, 'wb') as fh:
        fh.write(img_bytes)

def make_filename(url: str) -> str:
    rx = re.compile(r'\/([\w-]+)\.jpg$')
    match = rx.search(url)
    if match:
        return match.group(1) + '.jpg'

async def download_one(session: aiohttp.ClientSession, url: str, output_dir: str) -> None:
    img_bytes = await download_image(session, url)
    if img_bytes:
        filename = make_filename(url)
        await write_to_file(output_dir + filename, img_bytes)

async def download_all(urls: List[str], output_dir: str) -> None:
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[download_one(session, url, output_dir) for url in urls])
