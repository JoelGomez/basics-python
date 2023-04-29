"""
In programming, you often want to execute a block of code multiple times. To do so, you use a for loop.
"""

for n in range(10):
    print(n)


for n in range(1,11):
    print(n)


for n in range(1, 11, 2):
    print(n)

# for anidados
for a in range(1, 11):
    for b in range(2,4):
        print(f'{a} x {b} =', a * b )
