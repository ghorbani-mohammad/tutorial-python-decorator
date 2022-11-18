# lets start creating decorators


def my_decorator(func):
    def wrapper():
        print("Something is happening before the functions is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper  # Remember that we could return function from function


def say_whee():
    print("Whee!")


# we can decorate our function in the way
say_whee = my_decorator(say_whee)
print(say_whee)

say_whee()
