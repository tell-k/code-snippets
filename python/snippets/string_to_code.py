# -*- coding: utf-8 -*-

classname = "Saiyan"
saiyan_name = "Kakarot"

template = """
# -*- coding: utf-8 -*-

class %(classname)s(object):

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return 'Hello! My Name is ' + self.name

kakarot = %(classname)s("%(saiyan_name)s")
""" % locals()

try:
    exec template
except SyntaxError as e:
    raise SyntaxError(e)

print kakarot.say_hello() #=> Hello! My Name is Kakarot

raditz = Saiyan("Raditz")
print raditz.say_hello() #=> Hello! My Name is Raditz
