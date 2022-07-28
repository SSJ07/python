## in pyhton function is defined by using def keyword

def sayHello():
    print "Hello"


sayHello()


def outer_function():
    print "outer function"

    def inner_function():
        print "this is inner function"

    inner_function()

outer_function()

def add(x, y):
    return x + y
print add(4,5)
