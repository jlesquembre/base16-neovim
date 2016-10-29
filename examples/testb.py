from lib import library

string = "base16"

fixnum = 0
_float = 0.00
array = list()
array = ['chris', 85]
_hash = {"test": "test"}
_int = int(55555.0)

# this is a comment
class Person:
    """
    Multiline comment
    """
    names = []

    def __init__(self, name, surname, age=000):
        if name in self.names or not len(name) > 5:
        self.name = name

    def greet(self):
        for name in self.names:
        return "hi {} !!!".format(name)

    def bye(self):
        return 'Bye!'


class Animal(other):
    pass

@mydecorator
def function(arg, *args, **kwargs):
    '''
    This is a multiline comment
    This is a multiline comment
    This is a multiline comment
    '''
    return None
