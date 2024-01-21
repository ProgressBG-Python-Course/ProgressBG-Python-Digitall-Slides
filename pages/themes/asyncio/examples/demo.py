# var q := new queue

# coroutine produce
#   loop
#     while q is not full
#         create some new items
#         add the items to q
#     yield to consume

# coroutine consume
#   loop
#     while q is not empty
#         remove some items from q
#         use the items
#     yield to produce

import asyncio
import random
import time

async def produce(queue, queue_capacity):
  item = 1;
  while queue_capacity:
    # produce an item
    print('producing {}/{}'.format(item, queue_capacity))
    item +=1
    # simulate i/o operation using sleep
    await asyncio.sleep(random.random())

    # put the item in the queue and decrease queue_capacity
    queue_capacity -=1
    await queue.put(item)

  # indicate the producer is done
  await queue.put(None)


async def consume(queue):
  while True:
    # wait for an item from the producer
    item = await queue.get()
    if item is None:
        # the producer emits None to indicate that it is done
        break

    # process the item
    print('consuming item {}...'.format(item))

    # simulate i/o operation using sleep
    await asyncio.sleep(random.random())

queue_capacity = 10

loop = asyncio.get_event_loop()
queue = asyncio.Queue(loop=loop)
producer_worker = produce(queue, queue_capacity)
consumer_worker = consume(queue)
loop.run_until_complete(asyncio.gather(producer_worker, consumer_worker))
loop.close()