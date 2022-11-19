# In this step we want get information about the function (like memory location), not the decorator


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


# Above code is the decorator for running a function twice that
# we created in the previous examples


@do_twice
def say_whee():
    print("Whee!")


# The issue is that if we inspect the say_whee function
# we get information about the wrapper function not say_whee
# function. So the purpose is getting information about say_whee
# function.

# If we inspect the say_whee function in the below way:
print(say_whee)
# we get something like this:
# <function do_twice.<locals>.wrapper_do_twice at 0x10e9cc478>


# We can solve the issue in this way:
import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice
