import aiofiles
import asyncio

async def write_to_file(filename, data):
    async with aiofiles.open(filename, mode='w') as f:
        await f.writelines(data)

data = [
	'Line 1',
	'Line 2',
	'Line 3',
	'Line 4',
	'Line 5',
]
filename = './data.txt'
asyncio.run(write_to_file(filename, data))
print('END')