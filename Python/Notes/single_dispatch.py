
from functools import singledispatch
 
 
@singledispatch
def format_value(argument):
    raise ValueError("Cannot write for {} type".format(type(argument)))

# REMEMBER: format_value = singledispatch(format_value)

#           calling format_value actually calls the "wrapper"
#           method inside of single_dispatch,
#
#    def wrapper(*args, **kw):
#        if not args:
#            raise TypeError(f'{funcname} requires at least '
#                            '1 positional argument')
#
#        return dispatch(args[0].__class__)(*args, **kw)


"""
Decorators MUST BE A CALLABLE FUNCTION, therefore this method works as so,

def register(cls, func=None):
    if func is None:         <------ func = None if using decorator
        if isinstance(cls, type):
            return lambda f: register(cls, f)
                             int ------^   ^------ format_int

            
            @format_value.register(int)
            @wrapper.register(int)
            @lambda f: register(cls, f)
                    ^--> Decorator callable, so f = format_int
        =>  format_int = register(int, format_int)
        
        Now "[int] = format_int" is inside the registry
        defined inside the singledispatch scope. From here,
        you call format_value(5), NOT format_int. However
        register(int, format_int) returns format_int, therefore
        format_int(5) directly calls format_int
"""
@format_value.register(int)
def format_int(value):
    return f'Value = {value}: Type = int'

"""
OR we can call register directly as such to register
the type -> method
"""
def format_str(value):
    return f'Value = {value}: Type = str'
format_value.register(str, format_str)

"""
Type annotation for the first argument is an alternative
method to specifying the type for the method. Inside the register method
it will access the annotations from "ann = getattr(cls, '__annotations__', {})"
to grab "float" and access it to the function. Therefore, type annotations
can be used by the Python itself and not only third party tools like IDE's.
"""
@format_value.register
def format_float(value: float):
    return f'Value = {value}: Type = float'

print(format_value("123")) # Value = 123: Type = str
print(format_value(456))   # Value = 456: Type = int
print(format_value(5.5))   # Value = 5.5: Type = float

"""
Single dispatch utilizes decorators and the fact that "everything" is
an object in Python to add attributes to the function.

format_value = singledispatch(format_value)

When we call format_value, we call 

    def wrapper(*args, **kw):
        if not args:
            raise TypeError(f'{funcname} requires at least '
                            '1 positional argument')
        return dispatch(args[0].__class__)(*args, **kw)
        
where it will call the registered type to a method from dispatch.

Calling register can be simplified as "registry[cls] = func"
and calling format_value, which eventually calls dispatch
will work as "return registry[cls]"
"""
