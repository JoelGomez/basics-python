"""
Python while statement allows you to execute a code block 
repeatedly as long as a condition is True.
"""

while True:
    print ('Hola')
    break

age = 15

while age <=18:
    print(f"Edad = {age} Eres menor de edad")
    age += 2



age2 = 15
print('-' * 10)
while age2 <=18:
    print(f"Edad = {age2} Eres menor de edad")
    age2 += 2
else:
    print(f'Edad = {age2} Ya eres mayor de edad')


var = 1
while var > 0:
    print('este es un while que nunca se detendra')
