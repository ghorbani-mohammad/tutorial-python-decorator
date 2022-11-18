# In this example you can see how we can return value
# in a decorator


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)  # Notice that we have put return keyword in here

    return wrapper_do_twice


@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"


hi_adam = return_greeting("Adam")
print(hi_adam)
