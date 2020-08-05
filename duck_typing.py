# Duck typing and its easier to ask forgiveness than permissions
class Duck:
    def quack(self):
        print('quack quack')

    def fly(self):
        print('Flap Flap')


class Person:
    def quack(self):
        print('I am quacking like duck')

    def fly(self):
        print('I am flying like duck')


def quack_and_flying(thing):
    # Normal Way
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('It have to be Duck')

    # Look before you leap This is asking for permission

    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()

    # Asking forgiveness

    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)



d = Duck()
quack_and_flying(d)

p = Person()
quack_and_flying(p)
