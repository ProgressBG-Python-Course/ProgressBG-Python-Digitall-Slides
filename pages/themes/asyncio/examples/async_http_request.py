import asyncio
import aiohttp


@asyncio.coroutine
def do_request():
    response = yield from aiohttp.request(
        'GET', 'http://google.com',
    )
    return response

loop = asyncio.get_event_loop()
loop.run_until_complete(do_request())