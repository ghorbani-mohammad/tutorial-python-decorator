def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


# Notice that function are just objects like integer or string values in the memory
print(say_hello)  # By printing them you can check their location at memory

# You can add them to a list
my_list = [say_hello, be_awesome]
print(my_list[0])
print(my_list[0]("Mike"))


# We can also put functions into arguments of another function
def greet_bob(greeter_func):
    return greeter_func("Bob")


print(greet_bob(say_hello))
