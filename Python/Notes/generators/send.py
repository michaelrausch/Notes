"""
send() allows us to send a value to the generator.

The value will be received at the point where the last value was yielded.
"""
def double_inputs(x):
     while True:
          x = yield x * 2

gen = double_inputs(5)
"""
1. "gen" obtains the value of a generator object by calling double_inputs(5)
2. `next(gen)` will begin the code execution inside the generator function and 
   continue until a `yield` is hit and return that value. In this example
   the initial value of `x` is given as a parameter and immediately hits 
   `yield x * 2`, this means it will return the value of `5 * 2`.
3. At this point we can continue the generator code execution by using `next`
   or `send`. By using `next` we will receive an error, this is because the 
   value of `x` is being assigned to the return value of `yield x * 2`, which
   is `None`. The error happens when the line execution continues and it 
   attempts to perform `None * 2`. This is where `send` is utilized, `send` will
   pass the given value, assign it to the return value of `yield x * 2`, 
   therefore assigning it to the value of `x` and continue the generator
   code execution until the next `yield` is hit. In this case the first
   `gen.send(10)` call will assign `x` the value of 10, continue the `while`
   loop and `yield 10 * 2`, therefore returning 20 and pausing the generator
   code execution until either another `send` or `next` is called.
"""
print(next(gen))    # Prime generator, receive default value * 2, i.e. 10
print(gen.send(25)) # 50
print(gen.send(75)) # 150

"""
"send" is also extremely useful when writing coroutines.
Let's first look at this example,
"""

def coroutine():
     for i in range(1, 10):
          print(f"From generator:  {yield i}")
c = coroutine()
"""
Start the generator and obtain the value of the first yield, 1.
Pause execution until another `send` or `next` is called, this also
means we DO NOT perform the print statement.
"""
c.send(None)

"""
"sends" the new value in place of where the previously hit `yield` was 
and continue. Therefore it will now print "From generator:  9000" and also
return the value of 2. This is because when we send 9000, it will complete
the print function, continue the `for` loop, assign `i` the value of 2 and then
hit `yield i` once again.
"""
c.send(9000) # Value = 2 | From generator:  9000
c.send(1337) # Value = 3 | From generator:  1337
c.send(9001) # Value = 4 | From generator:  9001

"""
However, notice how the control is being passed back and forth. I am sending
the generator values (9000, 1337 and 9001) while being returned values also (1, 
2, 3 and 4). This is the primary goal of coroutines, they're used for lots of 
things such as the framework `asyncio`.

A generator without a `send` method will appear one way,

          ==========       yield       ========
          Generator |   ----------->   | User |
          ==========                   ========
          
but with send it becomes two way,

          ==========       yield       ========
          Generator |   ----------->   | User |
          ==========    <-----------   ========
                           send 

This allows customization of generators behaviour on the fly and the generator
responding to the user.
"""

"""
!POSSIBLE MISTAKES!
"""
def double_number(number):
     while True:
          number *= 2
          yield number
          
c = double_number(4)
c.send(None) # 8
c.send(10)   # 16, not 20
c.send(2)    # 32, not 4
c.send(1)    # 64, not 2
"""
The problem here is that the value being received by "send" is not utilized.
We are calling `c.send(2)` to continue the generator but it is not being 
assigned to any values, i.e. `yield number` is having the `send` value being
placed here, but no variable assigned to it, therefore it will have no affect.

To fix this, we needed to assign a value, i.e. `number = yield number`
"""
