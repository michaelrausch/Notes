"""
Standard generator returned using the yield keyword.

When the interpreter sees the keyword `yield`, it treats the function 
differently. The function will now return a Generator object when the function 
is called. The returned Generator object will contain all of the necessary
methods such as __next__ and will keep track of the function state such
as the variable `i`. The interpreter will analyze the contents of the function
such as knowing we have a `for` loop and place it inside the Generator. When
calling `next`, the Generator object will know to continue the function 
execution until we hit another `yield`, in this case it will return the value 
hit.
"""
def gen_n(n):
    for i in range(n):
        yield i

"""
A custom range Generator with exact behaviour as the function above, but easily
illustrates the usage of __next__ and state tracking to further enhance
understanding of how the internals of the Generator class work. The Generator
object returned by a function when the `yield` keyword is used, can be found at
the CPython source code at `/.../genobject.c`
"""
class RangeGenerator():
    
    def __init__(self, n):
        self.n = n
        self.current_n = 0
    
    """
    __iter__ defines a method on a class which will return an iterator (an 
    object that successively yields the next item contained by your object).
    
    The iterator object that __iter__() returns can be pretty much any object, 
    as long as it defines a __next__() method.
    """
    def __iter__(self):
        return self
        
    """
    The __next__() method will be called by statements like "for ... in ..." to 
    yield the next item, and __next__() should raise the StopIteration exception 
    when there are no more items.
    """
    def __next__(self):
        return self.next()
    
    def next(self):
        if self.current_n == self.n:
            raise StopIteration()
        rv = self.current_n
        self.current_n += 1
        return rv
    
for i in RangeGenerator(5):
    print(i)

print()
    
for i in gen_n(5):
    print(i)
