# Asynchronous code $3^{rd}$ party libraries

The main purpose of AsyncIO is to improve performance around asynchronous programming with the utilization of `async` and `await`. Continuing on my discussion inside of `threads/io_improvements.md`, it was understood that `isort.check_file` had IO Bound issues, therefore, could `asyncio` be useful to improve performance?

We have the function `isort.check_file` and we need this to behave in an asynchronous way. So, let us embed this inside a `async`.

```python
async def check_file(self, changed_file):
        return isort.check_file(changed_file)
```

Now, we need to pause for a moment and realize why this **will not work**. `isort.check_file` is a *synchronous function* - just wrapping it with `async` does not make it magically asynchronous. What our async function `check_file` is doing is just the same without `async` at the back. To get any meaningful performance asychronously, we **MUST be using some sort of** `Awaitable` - which requires the `await` keyword.

So basically what we did is equivalent to:

```python
import time

async def wait(n):
    time.sleep(n)
```

Which does absolutely no good for asynchronous operations.