import asyncio
import time

def sync_test():
    def sync_func(task_no):
        """ Synchronous function to simulate a task, taking 1 second """
        print(f'{task_no} is started ...')
        time.sleep(1)
        print(f'{task_no} ends!')

    def main():
        """  Main synchronous function to run multiple tasks. """
        taskA = sync_func('taskA')
        taskB = sync_func('taskB')
        taskC = sync_func('taskC')

    if __name__ == "__main__":
        time_start = time.time()
        main()
        time_end = time.time()

        print(f'Sync time: {time_end - time_start}')

    # taskA is started ...
    # taskA ends!
    # taskB is started ...
    # taskB ends!
    # taskC is started ...
    # taskC ends!
    # Sync time: 3.000988483428955

def async_test():
    async def async_func(task_no):
        """ Asynchronous function to simulate a task, taking 1 second """
        print(f'{task_no} is started ...')
        await asyncio.sleep(1)
        print(f'{task_no} ends!')

    async def main():
        """  Main asynchronous function to run multiple tasks concurrently. """
        taskA = asyncio.create_task(async_func('taskA'))
        taskB = asyncio.create_task(async_func('taskB'))
        taskC = asyncio.create_task(async_func('taskC'))
        await asyncio.wait([taskA, taskB, taskC])

    if __name__ == "__main__":
        time_start = time.time()
        asyncio.run(main())
        time_end = time.time()

        print(f'Async time: {time_end - time_start}')

    # taskA is started ...
    # taskB is started ...
    # taskC is started ...
    # taskA ends!
    # taskB ends!
    # taskC ends!
    # Took 1.0023751258850098



async_test()
sync_test()