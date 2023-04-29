"""
Sometimes, you want to terminate a for loop or a while loop 
prematurely regardless of the results of the conditional tests. 
In these cases, you can use the break statement:
"""

count = 5

for i in range(10):
    print(i)
    if i == count:
        break



count = 5
aux = 10

while True:
    print(aux)
    aux -= 1

    if count == aux:
        break


while True:
    age = int(input('Edad: ? '))

    if age < 18:
        continue
    else:
        print('Go')
        break