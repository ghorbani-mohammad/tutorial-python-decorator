# Here we want to have a look at inner functions topic
def parent():
    print("Printing from the parent function")

    def first_child():
        print("Printing from the first-child function")

    def second_child():
        print("Printing from the second-child function")

    second_child()
    first_child()


parent()

# Notice that below statement will raise exception because it's not defined.
# first_child()
# These function are reside inside the parent function locally.

# So the question is how we can have access to those local functions?
