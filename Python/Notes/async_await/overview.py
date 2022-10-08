import asyncio
import threading
import time

"""
The Python `asyncio` library was designed mainly for asynchronous IO operations like reading/writing files and 
network communications. The `async` and `await` keywords were introduced to prevent a heavy amount of callback
code structure, often referred to as callback hell. Instead using `async` / `await` presents the flow of a 
program in a sequential manner similar as if those asynchronous operations were blocking. Asynchronous code
is based around event loops, like UI frameworks, in this case `asyncio` has its own event loop and the 
keyword `await` are used to determine current resource allocation. When an `await` is reached, the code execution
will stop in that function and control is given back to the event loop to resume other asynchronous code, when
the `await`ed function has completed, it will be added back to the event loop queue and resumed when possible.

The `async` keyword wraps the function so that it now returns a coroutine object. The `await` keyword can be used to 
execute the coroutine in the blocking manner, or it can be added as a task to be executed later. `await` will
give control back to the event loop so other functions can be executed. Under the hood `asyncio` utilizes coroutines
for the internal implementation which also relies on generators, primarily the `send` method of generators.

Ideally, you want to utilize asynchronous programming when your script has I/O operations, where are are "waiting" for 
responses that are out of our control and give us the ability to perform other tasks while waiting. Yo do not want to 
use asynchronous code when you need a simple script with little to no I/O. Mixing `asyncio` with UI frameworks can be
a little tricky as `asyncio` will have its own event loop and so will other UI framework. Let us suppose we are mixing
`asyncio` and `tkinter`, running both event loops at the same time is a dubious proposition, but of course, can be done
if we mix both to use a single event loop.

It is very important to know that all of the code execution runs on a SINGLE THREAD, asynchronous programming
is a form of concurrency NOT parallelism. Here is a simple decision making on when to choose asynchronous programming,
multi-threading or multi-processing.

    if io_bound:
        if io_very_slow:
            print("Use Asyncio")
        else:
            print("Use Threads")
    else:
        print("Multi Processing")
        
    - CPU Bound => Multi Processing
    - I/O Bound, Fast I/O, Limited Number of Connections => Multi Threading
    - I/O Bound, Slow I/O, Many connections => Asyncio

Asynchronous vs Threads
-----------------------
- It is very difficult to write code that is thread safe. With Asynchronous code, you know exactly where the code will 
  shift from one task to the next and race conditions are therefore much harder to come by.
- Threads consume a fair amount of data since each thread needs to have its own stack. With async code, 
  all the code shares the same stack and the stack is kept small due to continuously unwinding the stack between tasks.
- Threads are OS structures and are therefore more memory for the platform to support. There is no such problem 
  with asynchronous tasks.
- Keep in mind Threads are not always identical between programming languages, this is because Threads may actually
  run in parallel in languages such as C++, but will not run in parallel in Python due to the Python GIL.
"""


async def await_blocking_example():
    print("Start blocking_example")
    await asyncio.sleep(2)
    print("Finished! blocking_example", end='\n\n')
    """
    Generally, when we call an asynchronous method the code execution
    will continue and the asynchronous call will be called when the 
    main script execution has paused and it has been given spare processing
    time to execute the asynchronous method. However, in this case
    "Finished!" will only print after two seconds.
    
    This is because the await keyword acts as a blocking call and pauses
    the main execution and waits for the coroutine to finish. During this time,
    it can allow for other coroutines to execute because of the "sleeping"
    call does not hold a lock. 

    The idea behind this example is that `print("Finished!...` would normally
    be executed in a callback function, but `await` is instead utilized to 
    prevent this and thus making the code much more readable.
    """


async def await_task_example():
    print("Start task_example")

    async def _task():
        print("Beginning task!")
        await asyncio.sleep(2)
        print("Completing task!")

    asyncio.create_task(_task())
    # Optionally, task = asyncio.create_task(...) and then "await task"

    print("Finished! task_example", end='\n\n')
    """
    To have "Finished!" print immediately, we need asyncio to instead
    create a task and not `await` it. This means that the given coroutine
    will be executed when the main script is complete/paused and can
    give processing power to any coroutines that need to be executed.
    """


async def async_execution_example():
    print("Start execution_example")

    async def _task():
        print("Beginning task execution_example!")
        await asyncio.sleep(2)
        print("Completing task! execution_example")

    asyncio.create_task(_task())
    await asyncio.sleep(2)
    print("Finished! execution_example")

    """
    Within this example, we notice that "Beginning task" has been ran
    before "Finished" has been done. This is happening because we
    call `asyncio.sleep` within this execution block. While we sleep
    in this execution, it means we can execute any waiting coroutines 
    that were added to the asyncio tasks to be ran at a later time. 
    This is crucial to understanding asynchronous programming, when 
    the `await` is hit, control is given back to the event loop to run 
    other tasks while we wait for the `await`ed function to complete.
    """


async def synchronous_blocking_in_async():
    """
    The purpose of this function is to illustrate that an async function
    is not ran inside of a new thread and when executed has the possibility
    of blocking the main UI thread if performing tasks for too long.
    """
    print("Current thread inside of async:", threading.get_ident())
    print("Main thread inside of async:", threading.main_thread(), end='\n\n')

    """
    This will block user interaction and freeze the UI, despite being
    inside an async function. Remember that the idea of asynchronous
    programming is to be different from sequential programming in that
    the async function will run "later" and is primarily used for prevention
    of waiting for blocking calls where we do not necessarily need to "wait",
    such as network requests, I/O operations or waiting for a user to select
    something on the UI.
    
    Blocking (CPU-bound) code should not be called directly. For example, 
    if a function performs a CPU-intensive calculation for 1 second, all
    concurrent asyncio Tasks and IO operations would be delayed by 1 second.

    An executor can be used to run a task in a different thread or even in a
    different process to avoid blocking the OS thread with the event loop. 
    See the loop.run_in_executor() method for more details.
    """
    print("Begin synchronous sleeping for 3 seconds")
    time.sleep(3)
    print("Completed synchronous sleeping for 3 seconds", end='\n\n')

async def main():
    # await await_blocking_example()
    # await await_task_example()
    # await async_execution_example()
    # await synchronous_blocking_in_async()
    pass


print("Current thread outside of async:", threading.get_ident())
print("Main thread outside of async:", threading.main_thread(), end='\n\n')
asyncio.run(main())
