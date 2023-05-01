"""
When you define a function, you can specify a default value for each 
parameter.
"""

def greet(name, lastname):
    print(f'hi {name} {lastname}')


greet('Joel', 'Gómez') #hi Joel Gomez


def greet2(name, lastname = 'Pérez'):
    print(f'hi {name} {lastname}')

greet2('Joel') #hi Joel Pérez
greet2('Joel','Romero') # hi Joel Romero


def greet(name='there', message='Hi'):
    return f"{message} {name}"

greeting = greet()
print(greeting)

