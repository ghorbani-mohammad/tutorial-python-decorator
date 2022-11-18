# In this example we can see how we can create
# decorator for functions that get argument


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")


greet("World")


@do_twice
def say_whee():
    print("Whee!")


say_whee()
