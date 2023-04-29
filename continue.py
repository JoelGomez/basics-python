"""
The continue statement is used inside a for loop or a while loop. 
The continue statement skips the current iteration and starts the next one.
"""

for i in range(1,21):
    if i % 2 == 0:
        print(i)
    else:
        continue


while True:
    val = int(input('cuanto es 13 * 12? '))
    if val != 156:
        continue
    else:
        break

for x in range(1,11):
    if x % 2 == 0:
        for y in range(1, 6):
            if y % 2 != 0:
                continue
            else:
                print(f'{x} * {y} = ', x * y )
