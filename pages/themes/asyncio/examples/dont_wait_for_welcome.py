import asyncio
from types import coroutine

async def couroutineA():
  # simulate i/o operation using sleep
  await asyncio.sleep(3)
  print("Welcome")


async def couroutineB():
  print("May I come in?")
  await couroutineA()
  print("NO, I WILL NOT WAIT!")



loop = asyncio.get_event_loop()
worker1 = couroutineA()
worker2 = couroutineB()

loop.run_until_complete(asyncio.gather(worker1, worker2))
loop.close()