"""
Sometimes, you need to perform a task multiple times in a 
program. And you don't want to copy the code for that same 
task all over places.
"""

def say_hello():
    print("Hi")

say_hello()


def greet(name):
    print('Hi', name)

greet('Luis')
greet('Jaime')



x = 5
def fun():
    x = 10
    print(x)

print(x)
fun()


def sum(a, b):
    return(a + b)

print(sum(5,6))