import asyncio

async def coroutine1():
	print('coroutine1 start')
	r = await foo()
	print('coroutine1 end')
	return r

async def foo():
	print('foo start')
	await asyncio.sleep(2)
	print('foo end')
	return 2

asyncio.run(coroutine1())