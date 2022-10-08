import asyncio

from common import function_execution_timer_async, network_request_one_second_sync


async def mistake_two():
    """
    This code illustrates usage of `async` / `await`, however it is incorrectly utilized and therefore does not give
    the potential benefits of asynchronous programming.

    Here, we correctly use `asyncio.gather` to run our asynchronous functions, `network_request_one_second_sync` is
    decorated with `async`. However, notice how this function takes 3 seconds instead of the expected 1 second to
    run to finish, something is wrong here!

    Remember, it is running in a single thread. AsyncIO is built on top of generators under the hood and not threads.
    Secondly `sleep()` from `time` module is blocking but `sleep()` from `asyncio` module is not - it gives
    control back to the event loop and schedules continuation of coroutine after given amount of time elapses.

    Therefore, the issue here is using `sleep()` from the `time` module and not allowing other tasks to execute
    when `waiting`, `sleep` from the `asyncio` is different and allows other tasks to run by giving control back
    to the event loop.
    """
    response = asyncio.gather(network_request_one_second_sync("uri/1"),
                              network_request_one_second_sync("uri/2"),
                              network_request_one_second_sync("uri/3"))
    return response


function_execution_timer_async(mistake_two)  # mistake_two took 3.019665241241455 seconds to execute, not 1 second!
