import asyncio
from common import function_execution_timer_async, network_request_one_second_async

network_request_one = "/one"
network_request_two = "/two"
network_request_three = "/three"


async def mistake_one():
    """
    The first common mistake with asynchronous programming is failing to run concurrently when given the opportunity.

    In this example we "await" the network requests, this means we wait for the response before we continue (Similar
    to synchronous blocking code). However, network request two and three do not need data / information from the
    response to network request one, therefore it is perfectly fine to continue to run asynchronously, that is
    we can execute network request one and while it is waiting for the response we can execute other tasks in the 
    meantime by giving control back to the event loop. The current code approach is necessary if the response
    from further network requests are dependent on earlier requests.
    """
    network_response_one = await network_request_one_second_async(network_request_one)
    network_response_two = await network_request_one_second_async(network_request_two)
    network_response_three = await network_request_one_second_async(network_request_three)
    return [network_response_one,
            network_response_two,
            network_response_three]


async def mistake_one_corrected():
    """
    To code this correctly, instead of `await`ing each network request, utilize the asyncio function
    gather. By utilizing asyncio.gather we will correctly free up resources when "waiting".

    When a coroutine comes across a blocking code (I/O, sleep), the current coroutine gets suspended and
    control is passed back to the event loop.

    It is running in a single thread. AsyncIO is built on top of generators under the hood and not threads.
    Secondly `sleep()` from `time` module is blocking but `sleep()` from `asyncio` module is not - it gives
    control back to the event loop and schedules continuation of coroutine after given amount of time elapses.
    """
    network_response_one = network_request_one_second_async(network_request_one)
    network_response_two = network_request_one_second_async(network_request_two)
    network_response_three = network_request_one_second_async(network_request_three)
    response = await asyncio.gather(network_response_one,
                                    network_response_two,
                                    network_response_three)
    return response


# Correct implementation tripled the function speed
function_execution_timer_async(mistake_one)            # mistake_one took 3.0201032161712646 seconds to execute
function_execution_timer_async(mistake_one_corrected)  # mistake_one_corrected took 1.010568618774414 seconds to execute
