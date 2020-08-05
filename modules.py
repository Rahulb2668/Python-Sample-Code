import LEGB as l

l.test()
l.test2()
l.test3()

# Enclosing Variable


def outer():
    x = 'Outer variable'

    def inner():
        x = 'Inner variable'
        print(x)

    inner()
    print(x)


outer()


def outer1():
    x = 'Outer variable'

    def inner1():
        nonlocal x
        x = 'Inner variable'
        print(x)

    inner1()
    print(x)


outer1()

