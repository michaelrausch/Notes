import asyncio
from time import time, sleep


def function_execution_timer_sync(func):
    start = time()
    func()
    end = time()
    print(f"{func.__name__} took {end - start} seconds to execute")


def function_execution_timer_async(func):
    start = time()
    asyncio.run(func())
    end = time()
    print(f"{func.__name__} took {end - start} seconds to execute")


async def network_request_one_second_async(uri):
    await asyncio.sleep(1)
    return "Network Response: " + uri


async def network_request_one_second_sync(uri):
    sleep(1)
    return "Network Response: " + uri
