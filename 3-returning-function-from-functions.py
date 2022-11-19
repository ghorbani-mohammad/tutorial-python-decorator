# Returning functions from functions
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)

print(first)  # <function parent.<locals>.first_child at 0x1010101>
print(second)  # <function parent.<locals>.second_child at 0x1010101>
print(first())
print(second())


# So you can return a function from a function
