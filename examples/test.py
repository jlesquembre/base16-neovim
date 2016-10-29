from lib import library

string = "base16"

fixnum = 0
_float = 0.00
array = list()
array = ['chris', 85]
_hash = {"test": "test"}

# this is a comment
class Person(object):
    """
    Multiline comment
    """
    names = []

    def __init__(self, name):
        if name not in self.names or len(name) > 5:
        self.name = name

    def greet(self):
        for name in self.names:
        return "hello {}".format(name)


class Animal(other):
    pass

@mydecorator
def function(arg, *args, **kwargs):
    '''
    This is a multiline comment
    '''
    return None

person1 = Person(name="Chris")
print(person1.greet(), "", person1.name, "\n")
