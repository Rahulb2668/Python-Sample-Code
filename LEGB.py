# LEGB
# Local Enclosing Global Builtins


# Global Variable

x = 'Global Variable x'

if __name__ == '__main__':
    print(x)


def test():
    y = 'local variable y'  # Local variable y
    print(y)
    print(x)  # Global x will be accessed if you don't have it in the local scope


def test2():
    x = 'Local variable x'
    print(x)


def test3():
    global x
    x = 'Reassigned global x'
    print(x)


if __name__ == '__main__':
    test()
    test2()
    test3()
    print(x)



